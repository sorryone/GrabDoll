# -*- coding: utf-8 -*-

from grabDoll.action.user_action import UserAction
from grabDoll.action.friend_action import FriendAction
from grabDoll.action.platform_action import PlatformAction
from grabDoll.action.formation_action import FormationAction
import uuid
__author__ = 'du_du'


def get_rank_info(uid, open_key, platform):
    friend_list = get_my_friend_list(uid, open_key, platform)
    top_list = get_top_100_list(uid)
    all_list = set(top_list + friend_list)
    list_info = get_my_friend_platform_info(uid, list(all_list))
    f_list = [f_id for f_id in friend_list if f_id in list_info]
    print set(friend_list) - set(f_list)
    return {
        'my_rank': 10111,
        'friend_list': f_list,
        'all_list': top_list,
        'list_info': list_info,
    }


def get_top_100_list(uid):
    # 获取全区前100的 用户ID
    res = list()
    return res


def test_uuid(openid, platform):
    uu = uuid.uuid3(openid + platform)
    return uu


# 我的好友列表
def get_my_friend_list(uid, open_key, platform):
    from grabDoll.logics import platform_logic
    data = platform_logic.get_app_friends(uid, open_key)
    app_friends = [str(item['openid'])for item in data.get('items', [])]
    f_action = FriendAction(uid)
    f_data = f_action.get_model_info()
    game_fri_list = [f_id for f_id in f_data.keys()]
    from grabDoll.action.account_action import AccountAction
    # 需要获得一个用户的游戏里的唯一ID
    a_action = AccountAction('')
    app_account_ids = a_action.get_all_by_app_uid(app_friends, {a_action.platform_str: platform})
    all_data = list(set(app_account_ids + game_fri_list))
    all_data.append('VIP')
    return all_data


def get_my_rank_info(uid):
    res = dict()
    return res


# 我的好友平台信息列表
def get_my_friend_platform_info(uid, fir_list):
    p_action = PlatformAction(uid)
    u_action = UserAction(uid)
    f_action = FormationAction(uid)
    p_info_data = p_action.get_all_by_userlist(fir_list)
    u_info_data = u_action.get_all_by_userlist(fir_list)
    r_info_data = f_action.get_all_by_userlist(fir_list)

    p_dict_info = {}
    for data in p_info_data:
        p_dict_info[data['u_id']] = data
    u_dict_info = {}
    for data in u_info_data:
        u_dict_info[data['u_id']] = data
    r_dict_info = {}
    for data in r_info_data:
        r_dict_info[data['u_id']] = data
    res = dict()
    for f_id in fir_list:
        item = {
            'id': f_id,
            'platform': p_dict_info.get(f_id, False),
            'userInfo': u_dict_info.get(f_id, False),
            'formation': r_dict_info.get(f_id, False),
        }
        if item.get('platform') is False or item.get('userInfo') is False:
            continue
        res[f_id] = item
    return res


# 我的好友列表信息
def get_list_info(data):
    res = list()
    for f_id in data:
        p_model = PlatformAction(f_id)
        u_model = UserAction(f_id)
        f_action = FormationAction(f_id)
        item = {
            'id': f_id,
            'platform': p_model.get_private_info(),
            'userInfo': u_model.get_private_info(),
            'formation': f_action.get_private_info(),
        }
        res.append(item)
    # res = sorted(res, key=lambda x: x['gold'], reverse=True)
    return res


# 我的好友列表信息
def get_my_friend_info(uid):
    action = FriendAction(uid)
    data = action.get_model_info()
    res = list()
    for f_id in data:
        p_model = PlatformAction(f_id)
        u_model = UserAction(f_id)
        f_action = FormationAction(f_id)
        p_model_info = p_model.get_private_info()
        item = {
            'id': f_id,
            'name': p_model_info['nickname'],
            'figureurl': p_model_info['figureurl'],
            'lv': u_model.get_value('lv'),
            'gold': u_model.get_gold(),
            'income': f_action.get_income(),
        }
        res.append(item)
    res = sorted(res, key=lambda x: x['gold'], reverse=True)
    return res


def get_my_rank_info(uid):
    res = dict()
    return res





