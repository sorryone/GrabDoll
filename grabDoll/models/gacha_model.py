# -*- coding: utf-8 -*-
from lib.redis_model import ListModel
import time
__author__ = 'du_du'


class GachaModel(ListModel):
    def get_model_info(self):
        return self.range(0, -1)

    # 增加物品
    def add_model(self, item_id, num=1):
        cur_models = self.length()
        print '当前gacha蛋的数量', cur_models

        # gacha蛋的数据结构
        data = {
            'id': item_id,
            't': time.time(),
            'ad': 0,
        }
        res = self.rpush(data)
        if res is not False:
            return True
        return False

    # 移除物品
    def remove_model(self, index):
        if index > self.length():
            return False
        gacha = self.index(index)
        res = self.trim(index, 1)
        print res
        if res == 0 or res is not False:
            return True
        return False

