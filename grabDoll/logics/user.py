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


def buy_vit(uid):
    add_ct = 10
    u = UserAction(uid)
    user_info = u.get_model_info()
    note_model = NoteModel(uid)
    cur_buy_ct = note_model.get_buy_vit_ct()
    price = 10
    cost = 2**cur_buy_ct * price
    cur_diamond = user_info.get(u.diamond_str, 0)
    if cur_diamond < cost:
        print (uid, u.diamond_str, 'not enough', cur_diamond, cost, cur_buy_ct)
        return False
    data = {
        u.diamond_str: cur_diamond - cost,
        u.vit_str: user_info.get(u.vit_str, 0) + add_ct
    }
    # 记录次数
    note_model.add_buy_vit_ct()
    res = {}
    if u.set_values(data):
        res['award'] = {'vit': add_ct}
    return res


def refresh_vit(uid):
    # 重置购买次数
    note_model = NoteModel(uid)
    last_refresh_time = note_model.get_vit_refresh_time()
    cur_time = time.time()
    today_zero_time = cur_time-cur_time % 86400 + time.timezone
    if last_refresh_time < today_zero_time:
        u = UserAction(uid)
        if u.get_vit() < u.max_vit_value:
            if note_model.reset_buy_vit_ct():    # if u.reset_vit():
                note_model.set_vit_refresh_time()
        else:
            note_model.set_vit_refresh_time()







