# -*- coding: utf-8 -*-

from grabDoll.action.user_action import UserAction
from grabDoll.action.friend_action import FriendAction
from grabDoll.action.platform_action import PlatformAction
from grabDoll.action.formation_action import FormationAction
__author__ = 'du_du'


def get_rank_info(uid):
    friend_list = get_my_friend_list(uid)
    top_list = get_top_100_list(uid)
    all_list = set(top_list + friend_list)
    return {
        'my_rank': 10111,
        'friend_list': friend_list,
        'all_list': top_list,
        'list_info': get_list_info(all_list),
    }


def get_top_100_list(uid):
    # 获取全区前100的 用户ID
    res = list()
    res.append('Test10')
    res.append('Test11')
    return res


# 我的好友列表
def get_my_friend_list(uid):
    action = FriendAction(uid)
    data = action.get_keys()
    return data


def get_my_rank_info(uid):
    res = dict()
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





