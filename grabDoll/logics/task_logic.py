# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.task_action import TaskAction
from grabDoll.logics import inventory_logic
import math
import time
import sys
__author__ = 'du_du'


def task_listen_result(func):
    def decorator(*args, **kwargs):
        res = func(*args, **kwargs)
        test_info(*args)
    return decorator


def test_info(data):
    print data


def get_task_info(uid):
    action = TaskAction(uid)
    return action.get_model_info()


def update_task_info(uid, action_type, task_target, task_value):
    config_model = ConfigModel('task')
    all_task_config_group = config_model.get_model_info()
    day_group = [key for key, x in all_task_config_group.items() if x.get('action_type', '') == action_type and x.get('mainType', '') == 'day']
    task_action = TaskAction(uid)
    cur_task_group = task_action.get_model_info()
    res = {}
    for task_id in day_group:
        cur_task_info = {}
        for task_info in cur_task_group:
            if task_info.get('key_id', 0) == task_id:
                cur_task_info = task_info
        cur_task_config = all_task_config_group.get(task_id)
        print cur_task_info.get('is_award', False), cur_task_config.get('action_value', 0), cur_task_info.get('t_value', 0)
        if cur_task_info.get('is_award', False) is False and cur_task_config.get('action_value', 0) > cur_task_info.get('t_value', 0):
            update_data = {'key_id': task_id, 't_value': cur_task_info.get('t_value', 0) + task_value}
            print (task_id, update_data)
            task_action.update_task_info_by_id(task_id, update_data)
            res[task_id] = update_data
    return res


def get_task_award(uid, task_id):
    task_action = TaskAction(uid)
    cur_task = task_action.get_task_info_by_id(task_id)
    if cur_task.get(task_action.is_award_str, True):
        return False
    config_model = ConfigModel('task')
    cur_task_config = config_model.get_config_by_id(task_id)
    if cur_task.get(task_action.value_str, 0) < cur_task_config.get('action_value', sys.maxint):
        return False
    res = []
    update_data = {task_action.is_award_str: True}
    if task_action.update_task_info_by_id(task_id, update_data) is True:
        res['update'] = update_data
    award = config_model.get('award', {}).encode('utf-8')
    award = eval(award)
    res['award'] = inventory_logic.add_awards(award)
    return res

