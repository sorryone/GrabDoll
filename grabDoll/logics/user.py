# -*- coding: utf-8 -*-
__author__ = 'maxijie'

from grabDoll.models.user import User


def set_userinfo(uid, data):
    if User.get(uid) is None:
        return False

    u = User(uid)
    u.set_values(data)
    return u


def get_userinfo(uid):
    if User.get(uid) is None:
        return False

    u = User(uid)
    return u.get_all()
