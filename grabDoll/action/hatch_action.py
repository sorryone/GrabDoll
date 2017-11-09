# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.handbook_model import HandBookModel, HandBookTable, HandBookTableSerializer
import time
__author__ = 'du_du'


class HatchAction(BaseModel):

    def __init__(self, u_id):
        self.u_id = u_id
        self.hatch_list = ('left', 'center', 'right')
        super(HatchAction, self).__init__(
                    u_id, HandBookModel, HandBookTable, HandBookTableSerializer, True)

    def get_model_info(self):
        data = self.get_all()
        res = dict()
        for key, value in data.items():
            res[key] = eval(value)
        return res

    # 增加物品
    def add_model(self, e_id):
        # 蛋的数据结构
        data = {
            "id": e_id,
            "t": time.time(),
            "ad": 0,
        }
        empty_hatch = [str(i) for i in self.hatch_list if self.get_value(i) != {}]
        print empty_hatch
        res = self.set_value(empty_hatch[0], data)
        if res is not False:
            return True
        return False

    # 移除物品
    def remove_model(self, index):
        res = self.set_value(self.hatch_list[index], '')
        if res == 0 or res is not False:
            return True
        return False

    def add_exp(self, index, exp):
        hatch_info = self.get_value(self.hatch_list[index])
        try:
            dict_data = eval(hatch_info)
        except Exception as e:
            print e
            pass
        cur_time = time.time()
        need_time = 300     # 需要的时间 先写死
        finish_time = float(dict_data['t']) + float(dict_data['ad']) + need_time
        print('当前时间戳', cur_time)
        print('预计时间', finish_time)
        print('存的时间', float(dict_data['t']))
        if cur_time < finish_time:
            dict_data['ad'] = float(dict_data['ad']) + int(exp)
            res = self.set_i(index, dict_data)
            print(res)
            if res == 0 or res is not False:
                return True
        return False
