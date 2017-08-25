# -*- coding: utf-8 -*-
from lib.redis_model import ListModel
import time
__author__ = 'du_du'


class GachaModel(ListModel):
    def get_model_info(self):
        res = self.range(0, -1)
        data_dict = dict()
        if type(res) is list:
            for index, value in res.iteritems():
                try:
                    model_info = eval(value)
                    data_dict[index] = model_info
                except Exception as e:
                    print e
                    continue
            return data_dict
        return self.range(0, -1)

    # 增加物品
    def add_model(self, item_id, num=1):
        # cur_models = self.length()
        # gacha蛋的数据结构
        data = {
            "id": item_id,
            "t": time.time(),
            "ad": 0,
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
        gachaStr = self.index(index)
        try:
            dict_data = eval(gachaStr)
        except Exception as e:
            print e
            pass
        cur_time = time.time()
        need_time = 300     # 需要的时间 先写死
        yuji_time = float(dict_data['t']) + float(dict_data['ad']) + need_time
        print '当前时间戳', cur_time
        print '预计时间', yuji_time
        print '存的时间', float(dict_data['t'])
        if cur_time < yuji_time:
            dict_data['ad'] = float(dict_data['ad']) + int(exp)
            res = self.set_i(index, dict_data)
            print res
            if res == 0 or res is not False:
                return True
        return False

