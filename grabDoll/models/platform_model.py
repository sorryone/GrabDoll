# -*- coding: utf-8 -*-
from lib.redis_model import StringModel, HashModel
__author__ = 'du_du'


class PlatformModel(HashModel):
    def get_model_info(self):
        data = self.get_all()
        return data


