# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.artifact_action import ArtifactAction
__author__ = 'du_du'


# 抓完娃娃后刷新当前的图鉴
def get_artifact_info(uid):
    # config_model = ConfigModel('artifact')
    action = ArtifactAction(uid)
    return action.get_model_info()


# 判定机器是否已经解锁
def check_book_unlock(uid, machine_id):
    pass

