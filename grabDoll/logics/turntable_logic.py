# -*- coding: utf-8 -*-
from grabDoll.logics import inventory_logic
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.user_action import UserAction
import random
__author__ = 'du_du'


# 抽取一次
def try_once(uid):
    gold_cost = 100
    u_action = UserAction(uid)
    if u_action.reduce_gold(gold_cost) is False:
        return False
    turntable_config_model = ConfigModel('turntable')
    turntable_config_info = turntable_config_model.get_model_info()
    random_list = []
    for key, value in turntable_config_info.items():
        random_list.extend([key] * value['chance'])
    selected_key = random.choice(random_list)
    selected_info = turntable_config_info[selected_key]
    print(selected_info)
    award = {selected_info['item_id']: int(selected_info['ct'])}
    res = {
        'selected': [selected_info['config_id']],
        'award': inventory_logic.add_awards(uid, award),
    }
    return res


# 抽取一次
def try_five_times(uid):
    gold_cost = 500
    u_action = UserAction(uid)
    if u_action.reduce_gold(gold_cost) is False:
        return False
    turntable_config_model = ConfigModel('turntable')
    turntable_config_info = turntable_config_model.get_model_info()
    random_list = []
    for key, value in turntable_config_info.items():
        random_list.extend([key] * value['chance'])
    selected_keys = random.sample(random_list, 5)
    awards = [{turntable_config_info[selected_key]['item_id']: int(turntable_config_info[selected_key]['ct'])} for selected_key in selected_keys]
    all_awards = union_dict(awards)
    res = {
        'selected': selected_keys,
        'award': inventory_logic.add_awards(uid, all_awards),
    }
    return res


def union_dict(data_group):
    _keys = set(sum([obj.keys() for obj in data_group], []))
    _total = {}
    for _key in _keys:
        _total[_key] = sum([obj.get(_key, 0) for obj in data_group])
    return _total

if __name__ == "__main__":
    print try_once('VIP')
