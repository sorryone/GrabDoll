# -*- coding: utf-8 -*-
from grabDoll.logics import user as user_logic
from grabDoll.logics import inventory_logic as inventory_logic
from grabDoll.logics import platform_logic as platform_logic
from grabDoll.logics import machine_logic as machine_logic
from grabDoll.logics import friend_logic as friend_logic
from grabDoll.logics import rank_logic as rank_logic
from grabDoll.logics import hatch_logic as hatch_logic
from grabDoll.logics import formation_logic as formation_logic
from grabDoll.logics import island_logic as island_logic
from grabDoll.logics import artifact_logic as artifact_logic
from grabDoll.logics import pve_logic as pve_logic
from grabDoll.logics import mail_logic as mail_logic
from grabDoll.models.note_model import NoteModel
from grabDoll.action.record_action import RecordAction
import time
__author__ = 'du_du'


def get_game_info(uid, open_key, is_debug=False):
    return False


def get_user_data(uid, open_key, is_debug=False):

    print('get_user_data', 'logic')
    platform_info = platform_logic.get_user_info_by_platform(uid, open_key, is_debug)
    if platform_info is False:
        return False

    # 当日首次登陆的检查
    note_model = NoteModel(uid)
    last_refresh_time = note_model.get_login_time()
    cur_time = time.time()
    today_zero_time = cur_time-cur_time % 86400 + time.timezone
    if last_refresh_time < today_zero_time:
        note_model.set_login_time()
        # 刷新体力
        user_logic.refresh_vit(uid)
    # 刷新收入
    island_logic.refresh_income_info(uid)

    refresh_config = {
        'income': 60,   # 收入刷新的间隔
        'vit': 3600,    # 体力刷新的时间
    }
    r_action = RecordAction(uid)
    r_info = r_action.get_model_info()
    return {
        'user': platform_info,
        'userInfo': user_logic.get_user_info(uid),
        'inventory': inventory_logic.get_inventory_info(uid),
        'machine': machine_logic.get_machine_info(uid),
        'note': machine_logic.get_note_info(uid),
        'hatch': hatch_logic.get_hatch_info(uid),
        'book': machine_logic.get_book_info(uid),
        'rank': rank_logic.get_rank_info(uid),
        'formation': formation_logic.get_formation_info(uid),
        'artifact': artifact_logic.get_artifact_info(uid),
        'pve': pve_logic.get_pve_info(uid),
        'mail': mail_logic.get_mail_info(uid),
        'refresh': refresh_config,
        'record': r_info,
    }


if __name__ == "__main__":
    # print get_game_info('ED57884CAA078DF9E0E08750D98CA834', 'F7D770DA0E6E8BDC6FF1D0A652925E2B')
    print get_user_data('VIP', 'VIP')

