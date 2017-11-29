# -*- coding: utf-8 -*-

from grabDoll.action.user_action import UserAction
from grabDoll.action.formation_action import FormationAction
import time
__author__ = 'du_du'


def refresh_income_info(uid):
    action = FormationAction(uid)
    info = action.get_model_info()
    print(info)
    capacity = info.get('capacity', 0)
    capacity_update_at = info.get('capacity_update_at', 0)
    income = info.get('income', 0)
    cur_time = int(time.time())
    # 每个小时的获取的金币
    per_hour_capacity = capacity / 10
    print(capacity, income, per_hour_capacity)
    income = int((cur_time - capacity_update_at) / 3600 * per_hour_capacity) + income
    res = {
        'income': income,
        'capacity_update_at': cur_time,
    }
    if action.set_values(res):
        print(res)
        return res
    return False


def award_income(uid):
    f_action = FormationAction(uid)
    u_action = UserAction(uid)
    income = f_action.get_income()
    res = dict()
    award = {}
    if f_action.set_income(0):
        res = u_action.add_gold(income)
        award['gold'] = income
    else:
        award['gold'] = 0
    return res
