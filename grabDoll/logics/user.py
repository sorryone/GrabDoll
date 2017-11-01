# -*- coding: utf-8 -*-
from grabDoll.action.user_action import UserAction
from grabDoll.models.note_model import NoteModel
__author__ = 'du_du'


def set_userinfo(uid, data):
    u = UserAction(uid)
    u.set_values(data)
    return u


# 添加
def add_awards(uid, data):
    u = UserAction(uid)
    for item, ct in data:
        u.incr(item, ct)
    return True


def get_user_info(uid):
    u = UserAction(uid)
    return u.get_model_info()

