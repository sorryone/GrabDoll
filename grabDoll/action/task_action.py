# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.task_model import TaskModel, TaskTable, TaskTableSerializer
import time
__author__ = 'du_du'


class TaskAction(BaseModel):

    def __init__(self, u_id):
        self.u_id = u_id
        self.pve_id_str = 'pve_id'
        self.modify_at_str = 'modify_at'
        self.value_str = 't_value'
        self.is_award_str = 'is_award'
        super(TaskAction, self).__init__(
                    u_id, TaskModel, TaskTable, TaskTableSerializer, True)

    def get_model_info(self):
        data = self.get_all()
        if isinstance(data, (list,)):
            return {}
        else:
            return data

    def get_task_info_by_id(self):
        data = self.get_all()
        return data

    def update_task_info_by_id(self, task_id):
        return True

    def get_award(self):
        return 0
