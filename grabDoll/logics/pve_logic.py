# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.pve_action import PveAction
from grabDoll.action.hero_action import HeroAction
from grabDoll.logics import formation_logic
__author__ = 'du_du'


def get_pve_info(uid):
    action = PveAction(uid)
    return action.get_model_info()


# 更新副本信息
def refresh_pve_info(uid):
    p_action = PveAction(uid)
    h_action = HeroAction(uid)
    pve_info = p_action.get_model_info()
    heroes = formation_logic.get_pve_heroes_info(uid)
    # 读取英雄属性配置信息
    hero_config = ConfigModel('doll')
    pve_config = ConfigModel('pve')
    hero_upgrade_config = ConfigModel('doll_upgrade')
    pve_config_info = pve_config.get_config_by_id(pve_info.get(pve_info.pve_id_str))
    print pve_config_info
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
    return alive_heroes

