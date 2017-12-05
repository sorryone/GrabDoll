# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.artifact_model import ArtifactModel, ArtifactTable, ArtifactTableSerializer
import time
import collections
__author__ = 'du_du'


class ArtifactAction(BaseModel):

    def __init__(self, u_id):
        self.u_id = u_id
        self.default_weapon = (30001, 30011, 30021, 30031, 30041)
        super(ArtifactAction, self).__init__(
                    u_id, ArtifactModel, ArtifactTable, ArtifactTableSerializer, True)

    def get_model_info(self):
        data_list = self.get_all()
        # 判定是否是新用户
        if len(data_list) == 0 and self.create_model():
            # 重新获取一次
            data_list = self.get_all()
        res = []

        return sorted(res, key=lambda x: x['key_id'], reverse=False)

    def get_model_info_by_id(self, w_id):
        data = self.get_all({"key_id": w_id})
        return data

    # 只有首次创建新用户初始化的时候调用
    def create_model(self):
        data = {
            "key_id": 0,
        }

        return self.set_values(data, data)



