# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.task_model import TaskModel, TaskTable, TaskTableSerializer
import time
import collections
__author__ = 'du_du'


class TaskAction(BaseModel):

    def __init__(self, u_id):
        self.u_id = u_id
        self.key_id_str = 'key_id'
        self.modify_at_str = 'modify_at'
        self.value_str = 't_value'
        self.is_award_str = 'is_award'
        super(TaskAction, self).__init__(
                    u_id, TaskModel, TaskTable, TaskTableSerializer, True)

    def get_model_info(self):
        data = self.get_all()
        res = []
        if len(data) == 0 and self.add_task(100005):
            # 重新获取一次
            data = self.get_all()
        if isinstance(data, (list,)):
            res = data
        elif isinstance(data, (dict, collections.OrderedDict)):
            res.append(data)
        return res

    def add_task(self, task_id):
        data = {self.key_id_str: task_id}
        return self.set_values(data, data)

    def get_task_info_by_id(self, task_id):
        data = self.get_all({self.key_id_str: task_id})
        return data

    def add_value(self, value, task_id):
        self.incr(self.value_str, value, {self.key_id_str: task_id})

    def update_task_info_by_id(self, task_id, update_info):
        return self.set_values(update_info, {self.key_id_str: task_id})

    def get_cur_task_group(self):
        data = self.get_all({self.is_award_str: 0})
        res = []
        if isinstance(data, (list,)):
            res = data
        elif isinstance(data, (dict, collections.OrderedDict)):
            res.append(data)
        return res
