# -*- coding: utf-8 -*-

from grabDoll.models.user import UserAction
from grabDoll.models.friend_model import FriendModel
from grabDoll.models.platform_model import PlatformAction
from grabDoll.models.base_model import BaseModel
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
    model = BaseModel(uid, FriendModel)
    data = model.hash_model.get_model_info()
    res = list()
    for f_id in data:
        p_model = BaseModel(f_id, PlatformAction)
        u_model = UserAction(f_id)
        item = {
            'id': f_id,
            'name': p_model.get_value('nickname').decode('utf-8'),
            'figureurl': p_model.get_value('figureurl'),
            'lv': u_model.get_value('lv')
        }
        res.append(item)
    return res


def get_my_rank_info(uid):
    res = dict()
    return res



