# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.task_action import TaskAction
import math
import time
__author__ = 'du_du'


def get_task_info(uid):
    action = TaskAction(uid)
    return action.get_model_info()

