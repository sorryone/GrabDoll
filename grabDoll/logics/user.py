# -*- coding: utf-8 -*-
from grabDoll.action.user_action import UserAction
from grabDoll.action.record_action import RecordAction
from grabDoll.models.config_model import ConfigModel
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


def add_exp(uid, add_value):
    u = UserAction(uid)
    info = u.get_model_info()
    cur_lv = info.get(u.lv_str, 1)
    cur_exp = info.get(u.exp_str, 0)
    latest_exp = cur_exp + add_value
    lv_config_model = ConfigModel('user_lv')
    cur_lv_config = lv_config_model.get_config_by_id(110000 + int(cur_lv))
    # 最高等级
    max_lv = 50
    data = dict()
    if cur_lv < max_lv and latest_exp >= cur_lv_config.get('exp', 0):
        data[u.lv_str] = cur_lv + 1
        data[u.exp_str] = latest_exp - cur_lv_config.get('exp', 0)
        if info.get(u.vit_str, 0) < 100:
            data[u.vit_str] = 100
    else:
        data[u.exp_str] = latest_exp
    if u.update_info(data):
        return data
    return False


def buy_vit(uid):
    add_ct = 10
    u = UserAction(uid)
    user_info = u.get_model_info()
    re_action = RecordAction(uid)
    record_info = re_action.get_model_info()
    cur_buy_ct = record_info.get(re_action.buy_vit_str, 0)
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
    re_action.update_model_info({re_action.buy_vit_str: cur_buy_ct+1})
    res = {}
    if u.set_values(data):
        res['award'] = {'vit': add_ct}
    return res


def refresh_vit(uid):
    u = UserAction(uid)
    if u.get_vit() < u.max_vit_value:
        u.reset_vit()







