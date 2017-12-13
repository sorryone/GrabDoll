# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.pve_action import PveAction
from grabDoll.logics import formation_logic
__author__ = 'du_du'


def get_pve_info(uid):
    action = PveAction(uid)
    return action.get_model_info()


# 更新副本信息
def refresh_pve_info(uid):
    heroes = formation_logic.get_pve_heroes_info(uid)
    return heroes

