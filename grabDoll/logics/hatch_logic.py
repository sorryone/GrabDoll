from grabDoll.action.hatch_action import HatchAction
__author__ = 'du_du'


def get_hatch_info(uid):
    action = HatchAction(uid)
    return action.get_model_info()
