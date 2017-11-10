# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.hatch_model import HatchModel, HatchTable, HatchTableSerializer
import time
import collections
__author__ = 'du_du'


class HatchAction(BaseModel):

    def __init__(self, u_id):
        self.u_id = u_id
        self.hatch_pos = (0, 1, 2)
        self.key_info = ('u_id', 'pos', 'key_id', 'ad', 'mark_at')
        super(HatchAction, self).__init__(
                    u_id, HatchModel, HatchTable, HatchTableSerializer, True)

    def get_model_info(self):
        data_list = self.get_all()
        res = []
        if isinstance(data_list, (dict, collections.OrderedDict)):
            res_item = self.filter_data(data_list)
            res.append(res_item)
        else:
            # 如果是数组
            for index, data in enumerate(data_list):
                res_item = self.filter_data(data)
                res.append(res_item)
        return res

    def filter_data(self, data):
        res_item = dict()
        for key in self.key_info:
            if key in data:
                res_item[key] = data[key]
        return res_item

    # 只有首次创建新用户初始化的时候调用
    def create_model(self):
        data = {
            "pos": 0,
        }
        return self.set_values(data, {"pos": 0})

    def hatch_unlock(self, index):
        if index == 0 or index not in self.hatch_pos:
            print 'index error'
            print type(index)
            return False
        data = {
            "pos": index,
        }
        if self.set_values(data, {"pos": index}):
            data_list = self.get_all({"pos": index})
            return self.filter_data(data_list)
        print 'db error'
        return False

    # 增加物品
    def add_model(self, key_id):
        # 蛋的数据结构
        data = {
            "key_id": key_id,
            "mark_at": time.time(),
            "ad": 0,
        }
        empty_hatch = [str(i) for i in self.hatch_pos if self.get_value(i) != {}]
        print empty_hatch
        res = self.set_value(empty_hatch[0], data)
        if res is not False:
            return True
        return False

    # 移除物品
    def remove_model(self, index):
        res = self.set_value(self.hatch_pos[index], '')
        if res == 0 or res is not False:
            return True
        return False

    def add_exp(self, index, exp):
        hatch_info = self.get_value(self.hatch_pos[index])
        try:
            dict_data = eval(hatch_info)
        except Exception as e:
            print e
            pass
        cur_time = time.time()
        need_time = 300     # 需要的时间 先写死
        finish_time = float(dict_data['mark_at']) + float(dict_data['ad']) + need_time
        print('当前时间戳', cur_time)
        print('预计时间', finish_time)
        print('存的时间', float(dict_data['mark_at']))
        if cur_time < finish_time:
            dict_data['ad'] = float(dict_data['ad']) + int(exp)
            res = self.set_value(index, dict_data)
            print(res)
            if res == 0 or res is not False:
                return True
        return False
