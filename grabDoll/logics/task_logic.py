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
    day_task_group = re_info.get(re_action.day_task_group_str)
    if day_task_group is None:
        day_task_group = []
    if str(task_id) in day_task_group:
        return False
    config_model = ConfigModel('task')
    cur_task_config = config_model.get_config_by_id(task_id)
    action_type = cur_task_config.get('action_type')
    action_target = cur_task_config.get('action_target')
    if action_target is not None and action_target != 0 and action_target != '':
        core_str = '%s_%s' % (action_type, action_target)
    else:
        core_str = action_type
    print core_str
    if re_info.get(core_str, 0) < cur_task_config.get('action_value', sys.maxint):
        return False
    res = {}
    day_task_group.append(task_id)
    update_data = {
        re_action.day_task_group_str: day_task_group,
        re_action.point_str: re_info.get(re_action.point_str) + cur_task_config.get('point', 0),
    }
    # if re_action.update_day_task_group(day_task_group) is True:
    if re_action.update_model_info(update_data) is True:
        res['update'] = task_id
    award = cur_task_config.get('award', {}).encode('utf-8')
    award = eval(award)
    from grabDoll.logics import inventory_logic
    res['award'] = inventory_logic.add_awards(uid, award)
    return res


def get_box_award(uid, box_id):
    re_action = RecordAction(uid)
    re_info = re_action.get_model_info()
    day_box_group = re_info.get(re_action.day_box_group_str)
    if day_box_group is None:
        day_box_group = []
    if str(box_id) in day_box_group:
        print 'box_id is haven'
        return False
    config_model = ConfigModel('box')
    box_config = config_model.get_config_by_id(box_id)
    if box_config.get('point') > re_info.get(re_action.point_str, 0):
        print 'point is not enough'
        return False
    res = {}
    day_box_group.append(box_id)
    if re_action.update_day_box_group(day_box_group) is True:
        res['update'] = box_id
    award = box_config.get('award', {}).encode('utf-8')
    award = eval(award)
    from grabDoll.logics import inventory_logic
    res['award'] = inventory_logic.add_awards(uid, award)
    return res
