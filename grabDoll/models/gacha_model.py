# -*- coding: utf-8 -*-
from lib.redis_model import ListModel
import time
__author__ = 'du_du'


class GachaModel(ListModel):
    def get_model_info(self):
        return self.range(0, -1)

    # 增加物品
    def add_model(self, item_id, num=1):
        # cur_models = self.length()
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
        res = self.remove(gacha)
        print res
        if res == 0 or res is not False:
            return True
        return False

    def add_exp(self, index, exp):
        if index > self.length():
            return False
        gacha = self.index(index)
        cur_time = time.time()
        need_time = 300     # 需要的时间 先写死
        yuji_time = float(gacha['t']) + float(gacha['ad']) + need_time
        if cur_time < yuji_time:
            gacha['ad'] = float(gacha['ad']) + int(exp)
            res = self.set_i(index, gacha)
            print res
            if res == 0 or res is not False:
                return True
        return False

