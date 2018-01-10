# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.task_action import TaskAction
from grabDoll.action.record_action import RecordAction
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


def get_task_award(uid, task_id):
    re_action = RecordAction(uid)
    re_info = re_action.get_model_info()
    day_task_group = re_info.get(re_action.day_task_group_str, [])
    if task_id in day_task_group:
        return False
    config_model = ConfigModel('task')
    cur_task_config = config_model.get_config_by_id(task_id)
    core_str = cur_task_config.get('action_type')
    if cur_task_config.get('action_target', None) is not None:
        core_str += '_' + cur_task_config.get('action_target', None)
    print core_str
    if re_info.get(core_str, 0) < cur_task_config.get('action_value', sys.maxint):
        return False
    res = {}
    day_task_group.append(task_id)
    if re_action.update_day_task_group(day_task_group) is True:
        res['update'] = task_id
    award = cur_task_config.get('award', {}).encode('utf-8')
    award = eval(award)
    from grabDoll.logics import inventory_logic
    res['award'] = inventory_logic.add_awards(award)
    return res

