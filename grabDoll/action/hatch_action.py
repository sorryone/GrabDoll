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
        # 判定是否是新用户
        if len(data_list) == 0 and self.create_model():
            # 重新获取一次
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
        full_length = len(self.hatch_pos)
        cur_length = len(res)
        # 填补未解锁的区域
        if cur_length < full_length:
            empty_list = [{'pos': self.hatch_pos[index]} for index in range(full_length) if index >= cur_length]
            res.extend(empty_list)
        return sorted(res, key=lambda x: x['pos'], reverse=False)

    def get_model_info_by_index(self, index):
        data = self.get_all({"pos": index})
        return data

    def get_hatch_available(self):
        data = self.get_model_info()
        item_list = [item for item in data if item['key_id'] == '']
        if len(item_list) > 0:
            return item_list[0]
        return None

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
        hatch_info = self.get_hatch_available()
        if hatch_info is not None and hatch_info is not {}:
            res = self.set_values(data, {'pos': hatch_info['pos']})
            if res is not False:
                data['pos'] = hatch_info['pos']
                return data
        return False

    def add_model_index(self, key_id, index):
        # 蛋的数据结构
        data = {
            "key_id": key_id,
            "mark_at": time.time(),
            "ad": 0,
        }
        res = self.set_values(data, {'pos': index})
        if res is not False:
            data['pos'] = index
            return data
        return False

    # 移除物品
    def remove_model(self, index):
        data = {
            "key_id": '',
            "mark_at": 0,
            "ad": 0,
        }
        res = self.set_values(data, {"pos": index})
        if res == 0 or res is not False:
            return True
        return False

    def add_exp(self, index, exp):
        hatch_info = self.get_model_info_by_index(self.hatch_pos[index])
        if hatch_info is None:
            print('not find hatch')
            return False
        if len(hatch_info) == 0:
            print('error hatch')
            return False
        cur_time = time.time()
        need_time = 3000     # 需要的时间 先写死
        finish_time = int(hatch_info['mark_at']) + int(hatch_info['ad']) + need_time

        if cur_time < finish_time:
            data = {
                "ad": int(hatch_info['ad']) + int(exp),
            }
            res = self.set_values(data, {'pos': hatch_info['pos']})
            print(res)
            if res == 0 or res is not False:
                hatch_info['ad'] = data['ad']
                return self.filter_data(hatch_info)
        return False
