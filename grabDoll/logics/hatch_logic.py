from grabDoll.action.hatch_action import HatchAction
from grabDoll.action.user_action import UserAction
from grabDoll.logics import machine_logic
__author__ = 'du_du'


def get_hatch_info(uid):
    action = HatchAction(uid)
    return action.get_model_info()


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

