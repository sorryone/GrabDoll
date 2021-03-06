# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.artifact_action import ArtifactAction
from grabDoll.action.item_action import ItemAction
from grabDoll.logics import record_logic
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
    check_data = action.get_model_info_by_id(artifact)
    if check_data is None or check_data is False or len(check_data) == 0:
        print('流氓数据 骗子')
        return False
    next_id = artifact_config.get('next_id')
    if next_id == -1:
        print('流氓数据 满级了')
        return False
    upgrade_item = artifact_config.get('upgrade')
    upgrade_items = eval(upgrade_item)
    item_model = ItemAction(uid)
    all_item_info = item_model.get_model_info()
    for a_id, ct in upgrade_items.iteritems():
        if int(all_item_info.get(a_id, 0)) < ct:
            print('消耗物品不够', a_id)
            return False
    for a_id, ct in upgrade_items.iteritems():
        remove_res = item_model.remove_model(a_id, ct)
        if remove_res is False:
            print (uid, '删除失败', a_id, ct)
    res = action.replace_model(artifact, next_id)
    if res:
        record_logic.add_record(uid, 'artifact', 1)
    return res


# 神器的能力
def get_artifact_akt(uid):
    action = ArtifactAction(uid)
    config_model = ConfigModel('artifact')
    artifact_group = action.get_model_info()
    all_atk = [int(config_model.get_config_by_id(c_id)['atk']) for c_id in artifact_group]
    res = {'atk': sum(all_atk)}
    return res





