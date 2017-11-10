from grabDoll.action.hatch_action import HatchAction
__author__ = 'du_du'


def get_hatch_info(uid):
    action = HatchAction(uid)
    return action.get_model_info()


def hatch_unlock(uid, index):
    action = HatchAction(uid)
    return action.hatch_unlock(index)


def hatch_speed(uid, index):
    action = HatchAction(uid)
    return action.add_exp(index, 100)
