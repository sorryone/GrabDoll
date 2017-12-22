# -*- coding: utf-8 -*-
from grabDoll.logics import inventory_logic
from grabDoll.models.config_model import ConfigModel
import random
__author__ = 'du_du'


# 抽取一次
def try_once(uid):
    turntable_config_model = ConfigModel('turntable')
    turntable_config_info = turntable_config_model.get_model_info()
    random_list = []
    for key, value in turntable_config_info.items():
        random_list.extend([key] * value['chance'])
    selected_key = random.choice(random_list)
    print(turntable_config_info[selected_key])
    return True
    award = []
    return inventory_logic.add_awards(uid, award)


# 抽取一次
def try_five_times(uid):
    return True

if __name__ == "__main__":
    print try_once('VIP')
