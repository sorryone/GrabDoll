# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.task_action import TaskAction
import math
import time
__author__ = 'du_du'


def get_task_info(uid):
    action = TaskAction(uid)
    return action.get_model_info()


def update_task_info(uid, action_type, task_target, task_value):
    print(action_type, task_target, task_value)
    config_model = ConfigModel('task')
    all_task_config_group = config_model.get_model_info()
    day_group = [key for key, x in all_task_config_group.items() if x.get('action_type', '') == action_type and x.get('mainType', '') == 'day']

    task_action = TaskAction(uid)

    cur_task_group = task_action.get_model_info()

    res = {}
    for task_id in day_group:
        cur_task_info = cur_task_group.get(task_id, {})
        cur_task_config = all_task_config_group.get(task_id)
        print cur_task_config
        if cur_task_info.get('is_award', False) and cur_task_config.get('action_value', 0) > cur_task_info.get('t_value', 0):
            update_data = {'key_id': task_id, 'action_value': cur_task_info.get('t_value', 0) + task_value}
            res[task_id] = update_data

    return res

