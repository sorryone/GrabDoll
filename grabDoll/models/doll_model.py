# -*- coding: utf-8 -*-
from lib.redis_model import StringModel, HashModel
__author__ = 'du_du'


class DollModel(HashModel):
    def get_model_info(self):
        return self.get_all()

    # 增加娃娃
    def add_model(self, item_id):
        # 娃娃的数据格式{'doll_id':40001,'exp':100,'lv':1,'state':0}
        doll = self.get_value(item_id)
        if doll is None:
            data = {'doll_id': item_id, 'exp': 0, 'lv': 1, 'state': 0}
        else:
            data = eval(doll)
            data['exp'] += 100
        res = self.set_value(item_id, data)
        print('add_model result', res)
        if res is not False:
            return data
        return False

    # 移除物品
    def reduce_model(self, item_id, num=1):
        cur_ct = self.get_value(item_id)
        if cur_ct < num:
            return False
        res = self.incr(item_id, -num)
        if res == 0 or res is not False:
            return True
        return False

