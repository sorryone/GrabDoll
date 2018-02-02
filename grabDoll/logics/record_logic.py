# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.task_action import TaskAction
from grabDoll.action.record_action import RecordAction
import math
import time
import sys
__author__ = 'du_du'


def add_record(u_id, action_str, ct):
    r_action = RecordAction(u_id)
    r_action.add_action_ct(action_str, ct)
    t_action = TaskAction(u_id)
    config_model = ConfigModel('task')
    task_config_groups = config_model.get_model_info()
    task_math_ids = [config_data.get('config_id') for config_data in task_config_groups.items() if
                     config_data.get('action_type') + config_data.get('action_target') == action_str]
    print task_math_ids
