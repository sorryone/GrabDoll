# -*- coding: utf-8 -*-
from grabDoll.logics import user as user_logic
from grabDoll.logics import inventory_logic as inventory_logic
import time
__author__ = 'du_du'


def get_game_info(uid):
    data = {
        'userInfo': user_logic.get_user_info(uid),
        'inventory': inventory_logic.get_inventory_info(uid),
        'config': {}
    }
    return data

