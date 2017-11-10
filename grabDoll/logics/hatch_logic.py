from grabDoll.action.hatch_action import HatchAction
from grabDoll.action.user_action import UserAction
__author__ = 'du_du'


def get_hatch_info(uid):
    action = HatchAction(uid)
    return action.get_model_info()


def hatch_unlock(uid, index):
    user_action = UserAction(uid)
    if user_action.reduce_diamond(100):
        action = HatchAction(uid)
        return action.hatch_unlock(index)
    print 'not diamond'
    return False


def hatch_speed(uid, index):
    action = HatchAction(uid)
    return action.add_exp(index, 100)
