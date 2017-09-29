# -*- coding: utf-8 -*-
from grabDoll.logics import user as user_logic
from grabDoll.logics import inventory_logic as inventory_logic
from grabDoll.logics import platform_logic as platform_logic
from grabDoll.logics import machine_logic as machine_logic
from grabDoll.logics import friend_logic as friend_logic
# import time
__author__ = 'du_du'


def get_game_info(uid, open_key):

    platform_info = platform_logic.get_user_info_by_platform(uid, open_key)
    if platform_info is False:
        return False
    return {
        'user': platform_info,
        'userInfo': user_logic.get_user_info(uid),
        'inventory': inventory_logic.get_inventory_info(uid),
        'config': inventory_logic.get_config_info(),
        'machine': machine_logic.get_machine_info(uid),
        'note': machine_logic.get_note_info(uid),
        # 'book': machine_logic.get_book_info(uid)
        # 'friend': friend_logic.get_my_friend_info(uid),
    }

if __name__ == "__main__":
    print get_game_info('ED57884CAA078DF9E0E08750D98CA834', 'F7D770DA0E6E8BDC6FF1D0A652925E2B')


