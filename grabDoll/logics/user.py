# -*- coding: utf-8 -*-
from grabDoll.models.user import User
__author__ = 'maxijie'


def set_userinfo(uid, data):
    if User.get(uid) is None:
        return False

    u = User(uid)
    u.set_values(data)
    return u


def create_user(uid):
    if User.get(uid) is None:
        return False
    data = {
        'gold': 1000,
        'diamond': 100,
        'uid': uid,
        'exp': 0,
        'lv': 1,
    }
    u = User(uid)
    u.set_values(data)


# 添加
def add_awards(uid, data):
    if User.get(uid) is None:
        return False

    u = User(uid)
    for item, ct in data:
        u.incr(item, ct)
    return True


def get_user_info(uid):
    if User.get(uid) is None:
        return False

    u = User(uid)
    return u.get_all()
