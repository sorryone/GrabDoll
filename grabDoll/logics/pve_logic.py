# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.pve_action import PveAction
from grabDoll.action.hero_action import HeroAction
from grabDoll.logics import formation_logic
import math
import time
__author__ = 'du_du'


def get_pve_info(uid):
    action = PveAction(uid)
    return action.get_model_info()


# 开启副本
def open_pve(uid):
    p_action = PveAction(uid)
    pve_info = p_action.get_model_info()
    is_start = pve_info.get(p_action.is_start_str)
    pve_config = ConfigModel('pve')
    if is_start is False:
        pve_config_info = pve_config.get_config_by_id(pve_info.get(p_action.pve_id_str))
    elif pve_info.get(p_action.is_award_str) is True:
        cur_pve_id = pve_info.get(p_action.pve_id_str)
        next_pve_id = cur_pve_id + 1
        pve_config_info = pve_config.get_config_by_id(next_pve_id)
    else:
        return False
    if pve_config_info is None:
        # 已经通关
        print 'pve is over'
        return False
    update_date = {
        p_action.pve_id_str: pve_config_info.get('config_id'),
        p_action.is_start_str: True,
        p_action.boss_hp_str: pve_config_info.get('hp', 999),
    }
    if p_action.set_values(update_date):
        return update_date
    return False


# 更新副本信息
def refresh_pve_info2(uid):
    p_action = PveAction(uid)
    h_action = HeroAction(uid)
    pve_info = p_action.get_model_info()
    heroes = formation_logic.get_pve_heroes_info(uid)
    # 读取英雄属性配置信息
    hero_config = ConfigModel('doll')
    pve_config = ConfigModel('pve')
    hero_upgrade_config = ConfigModel('doll_upgrade')
    pve_config_info = pve_config.get_config_by_id(pve_info.get(p_action.pve_id_str))
    alive_heroes = {}
    for hero_id, hero_info in heroes.iteritems():
        cur_hero_config = hero_config.get_config_by_id(hero_id)
        cur_lv_config = hero_upgrade_config.get_config_by_id(70000 + int(hero_info['lv']))
        base_atk = int(cur_hero_config['atk'])
        atk_add_per = int(cur_lv_config['add_atk'])
        hero_atk = base_atk * atk_add_per
        hero_max_hp = int(cur_hero_config['atk']) * float(cur_lv_config['add_atk'])
        hero_cur_hp = hero_max_hp - hero_info.get(h_action.loss_hp_str, 0)
        if hero_cur_hp > 0:
            alive_heroes[hero_id] = {'hp': hero_cur_hp, 'atk': hero_atk}
    average_atk = int(math.ceil(pve_config_info.get('atk')/float(len(alive_heroes))))
    boss_cur_hp = pve_config_info.get('hp') - pve_info.get(p_action.boss_hp_str, 0)
    print average_atk
    print boss_cur_hp
    return alive_heroes


# 更新副本信息
def refresh_pve_info(uid):
    p_action = PveAction(uid)
    pve_info = p_action.get_model_info()
    if pve_info.get(p_action.is_start_str) is not True or pve_info.get(p_action.is_award_str) is True:
        return False
    last_refresh_date = pve_info.get(p_action.modify_at_str, '')
    my_atk = formation_logic.get_pve_atk(uid)
    second = time.time() - (last_refresh_date/1000)
    if second < 10:
        print('net attack')
        return False
    print('second', second)
    print('my_atk', my_atk)
    rate = 60.0
    loss_hp = my_atk/rate * (second/rate)
    if my_atk <= 0:
        print('my_atk', my_atk)
        return False
    boss_cur_hp = pve_info.get(p_action.boss_hp_str, 0)
    if boss_cur_hp <= 0:
        print('boss_cur_hp', boss_cur_hp)
        # 已经凉了
        return False
    # 正常扣血
    last_hp = boss_cur_hp - loss_hp
    if p_action.set_hp(last_hp):
        pve_info[p_action.boss_hp_str] = last_hp
        return pve_info


def get_pve_award(uid):
    p_action = PveAction(uid)
    pve_info = p_action.get_model_info()
    if pve_info.get(p_action.is_start_str) is not True or pve_info.get(p_action.is_award_str) is True:
        return False
    if pve_info.get(p_action.boss_hp_str, 1) > 0:
        return False
    return True
