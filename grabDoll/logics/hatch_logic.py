# -*- coding: utf-8 -*-
from grabDoll.action.hatch_action import HatchAction
from grabDoll.action.user_action import UserAction
from grabDoll.logics import machine_logic
from grabDoll.models.config_model import ConfigModel
__author__ = 'du_du'


def get_hatch_info(uid):
    action = HatchAction(uid)
    res = action.get_model_info()
    return res


def hatch_unlock(uid, index):
    user_action = UserAction(uid)
    cost = 100
    if user_action.reduce_diamond(cost):
        action = HatchAction(uid)
        return action.hatch_unlock(index)
    print 'not diamond'
    return False


def hatch_speed(uid, index):
    user_action = UserAction(uid)
    cost = 100
    if user_action.reduce_gold(cost):
        action = HatchAction(uid)
        return action.add_exp(index, 100)
    print 'not gold'
    return False


def open_egg_by_cost(uid, index):
    action = HatchAction(uid)
    data = action.get_model_info_by_index(index)
    egg_id = data['key_id']
    egg_config_model = ConfigModel('egg')
    cur_egg_config = egg_config_model.get_config_by_id(egg_id)
    if cur_egg_config is False:
        return False
    open_type = cur_egg_config.get('open_type')
    open_cost = cur_egg_config.get('open_cost')
    user_action = UserAction(uid)
    if open_type == 'gold':
        check_cost = user_action.reduce_gold(open_cost)
    else:
        check_cost = user_action.reduce_diamond(open_cost)
    if check_cost is False:
        return False
    action = HatchAction(uid)
    if action.remove_model(index):
        return machine_logic.open_egg(uid, egg_id)
    else:
        return False


def hatch_open(uid, index):
    action = HatchAction(uid)
    data = action.get_model_info_by_index(index)
    egg_id = data['key_id']
    if action.remove_model(index):
        return machine_logic.open_egg(uid, egg_id)
    else:
        return False


def hatch_discard(uid, index):
    action = HatchAction(uid)
    data = action.get_model_info_by_index(index)
    egg_id = data['key_id']
    if egg_id != '':
        return action.remove_model(index)
    return False

