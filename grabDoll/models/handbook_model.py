# -*- coding: utf-8 -*-
from lib.redis_model import StringModel, HashModel
__author__ = 'du_du'


class HandBookModel(HashModel):
    def get_model_info(self):
        return self.get_all()

    # 增加物品
    def add_model(self, item_id, num=1):
        res = self.incr(item_id, num)
        if res is not False:
            return True
        return False

