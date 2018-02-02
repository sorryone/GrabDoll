# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.task_action import TaskAction
from grabDoll.action.record_action import RecordAction
from grabDoll.models.note_model import NoteModel
__author__ = 'du_du'


def add_record(u_id, action_str, ct):
    print ('add_record', action_str, ct)
    r_action = RecordAction(u_id)
    r_action.add_action_ct(action_str, ct)
    t_action = TaskAction(u_id)
    cur_task = t_action.get_cur_task_group()
    cur_task_ids = [task_info[t_action.key_id_str] for index, task_info in enumerate(cur_task)]
    task_data = {}
    for index, task_info in enumerate(cur_task):
        task_data[task_info[t_action.key_id_str]] = task_info

    config_model = ConfigModel('task')
    task_config_groups = config_model.get_model_info()
    task_math_ids = [config_id for config_id, config_data in task_config_groups.items() if
                     str(config_data.get('action_type')) + str(config_data.get('action_target')) == action_str and
                     config_data.get('mainType') != 'day' and
                     config_id in cur_task_ids]
    if len(task_math_ids) == 0:
        return 0
    task_id = task_math_ids[0]

    if task_config_groups[task_id]['mainType'] == 'guild' \
            and task_data[task_id][t_action.value_str] + ct >= task_config_groups[task_id]['action_value']:
        t_action.add_task(task_config_groups[task_id]['next_task'])
        update_data = {
            t_action.value_str: task_data[task_id][t_action.value_str] + ct,
            t_action.is_award_str: True
        }
        t_action.update_task_info_by_id(task_id, update_data)
        n_model = NoteModel(u_id)
        n_model.add_buy_vit_ct()
        print('add task', task_id)
    else:
        t_action.add_value(ct, task_id)
    return task_math_ids
