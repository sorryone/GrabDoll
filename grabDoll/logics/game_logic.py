# -*- coding: utf-8 -*-
from grabDoll.logics import user as user_logic
from grabDoll.logics import inventory_logic as inventory_logic
from grabDoll.logics import platform_logic as platform_logic

# import time
__author__ = 'du_du'


def get_game_info(uid, open_key):

    platform_info = platform_logic.get_user_info_by_platform(uid, open_key)
    if platform_info is False:
        return False
    data = {
        'user': platform_info,
        'userInfo': user_logic.get_user_info(uid),
        'inventory': inventory_logic.get_inventory_info(uid),
        'config': inventory_logic.get_config_info(),
    }
    return data
