# -*- coding: utf-8 -*-

from grabDoll.action.user_action import UserAction
from grabDoll.action.friend_action import FriendAction
from grabDoll.action.platform_action import PlatformAction
__author__ = 'du_du'


def get_rank_info(uid):
    return {
        'my_rank': 10111,
        'friend': get_my_friend_info(uid),
        'all': get_top_100_info(),
    }


def get_top_100_info():
    # 获取全区前100的 用户ID
    res = list()
    return res


# 我的好友列表信息
def get_my_friend_info(uid):
    action = FriendAction(uid)
    data = action.get_model_info()
    res = list()
    for f_id in data:
        p_model = PlatformAction(f_id)
        u_model = UserAction(f_id)
        p_model_info = p_model.get_private_info()
        item = {
            'id': f_id,
            'name': p_model_info['nickname'],
            'figureurl': p_model_info['figureurl'],
            'lv': u_model.get_value('lv'),
            'income': 100,
        }
        res.append(item)
    return res


def get_my_rank_info(uid):
    res = dict()
    return res



