# -*- coding: utf-8 -*-

from grabDoll.action.user_action import UserAction
from grabDoll.action.formation_action import FormationAction
import time
__author__ = 'du_du'


def refresh_income_info(uid):
    action = FormationAction(uid)
    info = action.get_model_info()
    print(info)
    capacity = info.get(action.capacity_str, 0)
    capacity_update_at = info.get(action.capacity_update_at_str, 0)
    if info.get(action.fight_state_str) == action.state_injured:
        return False
    cur_income = info.get(action.income_str, 0)
    cur_time = int(time.time())
    # 每个小时的获取的金币
    per_hour_capacity = capacity / 10.0
    income = int((cur_time - capacity_update_at) / 3600.0 * per_hour_capacity) + cur_income
    print(capacity, cur_income, per_hour_capacity, income)

    if income == cur_income:
        return False
    res = {
        'income': income,
        'capacity_update_at': cur_time,
    }

    if action.set_values(res):
        print(res)
        return res
    return False


def check_income(uid):
    action = FormationAction(uid)
    info = action.get_model_info()
    capacity = info.get('capacity', 0)
    capacity_update_at = info.get('capacity_update_at', 0)
    cur_income = info.get('income', 0)
    cur_time = int(time.time())
    # 每个小时的获取的金币
    per_hour_capacity = capacity / 10.0
    income = int((cur_time - capacity_update_at) / 3600.0 * per_hour_capacity) + cur_income
    print (cur_time - capacity_update_at)
    print(capacity, cur_income, per_hour_capacity, income)


def award_income(uid):
    f_action = FormationAction(uid)
    u_action = UserAction(uid)
    income = f_action.get_income()
    res = dict()
    award = {}
    if f_action.set_income(0):
        if u_action.add_gold(income):
            award['gold'] = income
        else:
            print('is db error')
    else:
        award['gold'] = 0
    res['award'] = award
    return res
