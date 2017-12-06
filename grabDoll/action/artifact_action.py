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
        self.key_str = 'key_id'
        super(ArtifactAction, self).__init__(
                    u_id, ArtifactModel, ArtifactTable, ArtifactTableSerializer, True)

    def get_model_info(self):
        data_list = self.get_all()
        # 判定是否是新用户
        if len(data_list) == 0:
            # 重新获取一次
            res = self.create_model()
        else:
            res = [int(item[self.key_str]) for item in data_list]
            res.sort()
            # res = sorted(res, key=lambda x: x['key_id'], reverse=False)
        return res

    def get_model_info_by_id(self, w_id):
        data = self.get_all({self.key_str: w_id})
        return data

    # 只有首次创建新用户初始化的时候调用
    def create_model(self):
        for key_id in self.default_weapon:
            data = {
                self.key_str: key_id,
            }
            self.set_values(data, data)
        return self.default_weapon

    def replace_model(self, previous, current):
        return self.set_values({self.key_str: current}, {self.key_str: previous})



