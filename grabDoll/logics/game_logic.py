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
from grabDoll.action.account_action import AccountAction
from grabDoll.logics import task_logic as task_logic
import time
__author__ = 'du_du'


def get_user_data(open_id, open_key, platform):
    start_time = time.time()
    platform_info = platform_logic.get_user_info_by_platform(open_id, open_key)
    if platform_info is False:
        return False
    # 需要获得一个用户的游戏里的唯一ID
    a_action = AccountAction('')
    game_user_id = a_action.get_model_info_by_id(open_id, platform)
    if game_user_id is False:
        game_user_id = a_action.create_model(open_id, platform)
    uid = game_user_id
    print('game_user_id', game_user_id)
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
    res = {
        'game_user_id': uid,
        'user': platform_info,
        'userInfo': user_logic.get_user_info(uid),
        'inventory': inventory_logic.get_inventory_info(uid),
        'note': machine_logic.get_note_info(uid),
        'rank': rank_logic.get_rank_info(uid, open_key),
        'formation': formation_logic.get_formation_info(uid),
        'artifact': artifact_logic.get_artifact_info(uid),
        'pve': pve_logic.get_pve_info(uid),
        'mail': mail_logic.get_mail_info(uid),
        'refresh': refresh_config,
        'record': r_info,
        'task': task_logic.get_task_info(uid),
    }
    print ('get_user_data cost time', time.time() - start_time)
    return res


def get_user_test(open_id, open_key, platform):
    start_time = time.time()
    platform_info = platform_logic.get_user_info_by_platform(open_id, open_key)
    if platform_info is False:
        return False
    time_str_0 = time.time()
    # 需要获得一个用户的游戏里的唯一ID
    a_action = AccountAction('')
    game_user_id = a_action.get_model_info_by_id(open_id, platform)
    if game_user_id is False:
        game_user_id = a_action.create_model(open_id, platform)
    uid = game_user_id
    time_str_1 = time.time()
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
    time_str_2 = time.time()
    user_info = user_logic.get_user_info(uid)
    inventory = inventory_logic.get_inventory_info(uid)
    note_info = machine_logic.get_note_info(uid)
    time_str_3 = time.time()
    ran_info = rank_logic.get_rank_info(uid, open_key)
    time_str_4 = time.time()
    formation_info = formation_logic.get_formation_info(uid)
    artifact_info = artifact_logic.get_artifact_info(uid)
    pve_info = pve_logic.get_pve_info(uid)
    mail_info = mail_logic.get_mail_info(uid)
    task_info = task_logic.get_task_info(uid)
    time_str_5 = time.time()
    res = {
        'game_user_id': uid,
        'user': platform_info,
        'user_info': user_info,
        'inventory': inventory,
        'note': note_info,
        'rank': ran_info,
        'formation': formation_info,
        'artifact': artifact_info,
        'pve': pve_info,
        'mail': mail_info,
        'refresh': refresh_config,
        'record': r_info,
        'task': task_info,
    }
    print('step0', time_str_0 - start_time)
    print('step1', time_str_1 - time_str_0)
    print ('step2', time_str_2 - time_str_1)
    print ('step3', time_str_3 - time_str_2)
    print ('step4', time_str_4 - time_str_3)
    print ('step5', time_str_5 - time_str_4)
    print ('get_user_data cost time', time.time() - start_time)
    return res


def get_user_first_data(open_id, open_key, platform):
    start_time = time.time()
    platform_info = platform_logic.get_user_info_by_platform(open_id, open_key)
    if platform_info is False:
        return False
    time_str_0 = time.time()
    # 需要获得一个用户的游戏里的唯一ID
    a_action = AccountAction('')
    game_user_id = a_action.get_model_info_by_id(open_id, platform)
    if game_user_id is False:
        game_user_id = a_action.create_model(open_id, platform)
    uid = game_user_id
    time_str_1 = time.time()
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
    time_str_2 = time.time()

    refresh_config = {
        'income': 60,   # 收入刷新的间隔
        'vit': 3600,    # 体力刷新的时间
    }
    time_str_3 = time.time()
    r_action = RecordAction(uid)
    r_info = r_action.get_model_info()
    user_info = user_logic.get_user_info(uid)
    inventory = inventory_logic.get_inventory_info(uid)
    note_info = machine_logic.get_note_info(uid)
    time_str_4 = time.time()
    artifact_info = artifact_logic.get_artifact_info(uid)
    pve_info = pve_logic.get_pve_info(uid)
    task_info = task_logic.get_task_info(uid)
    time_str_5 = time.time()
    res = {
        'game_user_id': uid,
        'user': platform_info,
        'user_info': user_info,
        'inventory': inventory,
        'note': note_info,
        'artifact': artifact_info,
        'pve': pve_info,
        'refresh': refresh_config,
        'record': r_info,
        'task': task_info,
    }
    print('step0', time_str_0 - start_time)
    print('step1', time_str_1 - time_str_0)
    print ('step2', time_str_2 - time_str_1)
    print ('step3', time_str_3 - time_str_2)
    print ('step4', time_str_4 - time_str_3)
    print ('step5', time_str_5 - time_str_4)
    print ('get_user_data cost time', time.time() - start_time)
    return res


def get_user_test(uid, open_key):
    start_time = time.time()
    machine_info = machine_logic.get_machine_info(uid)
    hatch_info = hatch_logic.get_hatch_info(uid)
    book_info = machine_logic.get_book_info(uid)
    ran_info = rank_logic.get_rank_info(uid, open_key)
    formation_info = formation_logic.get_formation_info(uid)
    pve_info = pve_logic.get_pve_info(uid)
    mail_info = mail_logic.get_mail_info(uid)
    res = {
        'machine': machine_info,
        'hatch': hatch_info,
        'book': book_info,
        'rank': ran_info,
        'formation': formation_info,
        'pve': pve_info,
        'mail': mail_info,
    }
    print ('get_user_data cost time', time.time() - start_time)
    return res


if __name__ == "__main__":
    # print get_game_info('ED57884CAA078DF9E0E08750D98CA834', 'F7D770DA0E6E8BDC6FF1D0A652925E2B')
    print get_user_data('VIP', 'VIP')

