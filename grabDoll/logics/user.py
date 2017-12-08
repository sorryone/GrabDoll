# -*- coding: utf-8 -*-
from grabDoll.action.user_action import UserAction
from grabDoll.models.note_model import NoteModel
import datetime
import time
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


def refresh_vit(uid):
    note_model = NoteModel(uid)
    last_refresh_time = note_model.get_vit_refresh_time()
    cur_time = time.time()
    today_zero_time = cur_time-cur_time % 86400 + time.timezone
    if last_refresh_time < today_zero_time:
        u = UserAction(uid)
        if u.get_vit() < u.max_vit_value:
            if u.reset_vit():
                note_model.set_vit_refresh_time()
        else:
            note_model.set_vit_refresh_time()







