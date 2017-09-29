# -*- coding: utf-8 -*-
from grabDoll.models.user import User as UserModel
from grabDoll.models.friend_model import FriendModel
from grabDoll.models.platform_model import PlatformModel
__author__ = 'du_du'


# 我的好友列表信息
def get_my_friend_info(uid):
    return {
        'friend': get_my_friend_info(uid)
    }


# 我的好友列表信息
def get_my_friend_info2(uid):
    model = FriendModel(uid)
    data = model.get_model_info()
    for f_id in data:
        p_model = PlatformModel(f_id)
        u_model = UserModel(f_id)
        data[f_id]['name'] = p_model.get_value('nickname')
        data[f_id]['figureurl'] = p_model.get_value('figureurl')
        data[f_id]['lv'] = u_model.get_value('lv')
    return data


# 进入好友家
def enter_friend_home(uid):
    model = FriendModel(uid)
    return model.get_model_info()


# 申请成为好友
def add_friend(uid, friend_id):
    model = FriendModel(uid)
    model.set_value(friend_id, {})
    return True


# 接受好友请求
def accept_friend(uid, friend_id):
    model = FriendModel(uid)
    model.set_value(friend_id, {})
    return True


# 拒绝好友请求
def refuse_friend(uid, friend_id):
    return True


# 移除好友
def remove_friend(uid, friend_id):
    model = FriendModel(uid)
    model.delete(friend_id)
    return True


if __name__ == "__main__":
    print get_my_friend_info('ED57884CAA078DF9E0E08750D98CA834')


