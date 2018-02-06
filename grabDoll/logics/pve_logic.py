# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.pve_action import PveAction
from grabDoll.action.hero_action import HeroAction
from grabDoll.logics import formation_logic
from grabDoll.logics import inventory_logic
from grabDoll.logics import record_logic
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
    """
    if update_date.get(p_action.pve_id_str) == p_action.default_pve_id:
        # 如果是新手
        update_date[p_action.boss_hp_str] = 0
    """
    if p_action.set_values(update_date):
        return update_date
    return False


# 更新副本信息
def refresh_pve_info(uid):
    p_action = PveAction(uid)
    pve_info = p_action.get_model_info()
    if pve_info.get(p_action.is_start_str) is not True or pve_info.get(p_action.is_award_str) is True:
        return False
    if pve_info.get(p_action.pve_id_str) == p_action.default_pve_id:
        # 如果是新手
        last_hp = 0
    else:
        last_refresh_date = pve_info.get(p_action.modify_at_str, '')
        second = time.time() - (last_refresh_date / 1000)
        if second < 10:
            print('net attack')
            return False
        print('second', second)
        my_atk = formation_logic.get_pve_atk(uid)
        print('my_atk', my_atk)
        if my_atk <= 0:
            print('my_atk', my_atk)
            return False
        rate = 60.0
        loss_hp = my_atk/rate * (second/rate)
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
    pve_config = ConfigModel('pve')
    pve_config_info = pve_config.get_config_by_id(pve_info.get(p_action.pve_id_str))
    award_item = pve_config_info.get('award')
    award_items = eval(award_item)
    res = dict()
    # 获取下一关的配置
    cur_pve_id = pve_info.get(p_action.pve_id_str)
    next_pve_id = cur_pve_id + 1
    pve_config_info = pve_config.get_config_by_id(next_pve_id)
    if formation_logic.set_explore(uid, ['', '', '', '', '']) is False:
        return False
    if pve_config_info is not None:
        update_date = {
            p_action.pve_id_str: pve_config_info.get('config_id'),
            p_action.boss_hp_str: pve_config_info.get('hp', 999),
            p_action.is_start_str: False,
            p_action.is_award_str: False,
        }
        res['pve'] = update_date
    else:
        update_date = {
            p_action.is_award_str: True,
        }
        pve_info[p_action.is_award_str] = update_date[p_action.is_award_str]
        res['pve'] = update_date
    if p_action.set_values(update_date):
        res['award'] = inventory_logic.add_awards(uid, award_items)
        record_logic.add_record(uid, 'pve', 1)
    return res

