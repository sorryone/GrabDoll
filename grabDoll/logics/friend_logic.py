# -*- coding: utf-8 -*-
from grabDoll.models.user import User as UserModel
from grabDoll.models.friend_model import FriendModel

__author__ = 'du_du'


# 我的好友列表信息
def get_my_friend_info(uid):
    model = FriendModel(uid)
    return model.get_model_info()


# 进入好友家
def enter_friend_home(uid):
    model = FriendModel(uid)
    return model.get_model_info()


# 申请成为好友
def add_friend(uid, friend_id):
    return True


# 接受好友请求
def accept_friend(uid, friend_id):
    return True


# 拒绝好友请求
def refuse_friend(uid, friend_id):
    return True


# 移除好友
def remove_friend(uid, friend_id):
    return True

