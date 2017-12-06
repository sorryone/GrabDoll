# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.artifact_action import ArtifactAction
__author__ = 'du_du'


# 抓完娃娃后刷新当前的图鉴
def get_artifact_info(uid):
    action = ArtifactAction(uid)
    return action.get_model_info()


# 判定机器是否已经解锁
def upgrade_artifact(uid, artifact):
    action = ArtifactAction(uid)
    config_model = ConfigModel('artifact')
    artifact_config = config_model.get_config_by_id(artifact)
    if artifact_config is False:
        print('流氓数据 错误的ID')
        return False
    next_id = artifact_config.get('next_id')
    if next_id == -1:
        print('流氓数据 满级了')
        return False
    return action.replace_model(artifact, next_id)



