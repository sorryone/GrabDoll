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

    update_task_list = [[task_id, ] for task_id in day_group]
    print update_task_list
    return cur_task_group
