# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.pve_action import PveAction
__author__ = 'du_du'


def get_pve_info(uid):
    action = PveAction(uid)
    return action.get_model_info()

