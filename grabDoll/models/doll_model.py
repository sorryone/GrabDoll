# -*- coding: utf-8 -*-
from lib.redis_model import StringModel, HashModel
__author__ = 'du_du'


class DollModel(HashModel):
    def get_model_info(self):
        return self.get_all()

    def get_doll_keys(self):
        return self.get_keys()

    def get_doll_group(self):
        doll_keys = self.get_keys()
        my_doll_keys = [str(i) for i in doll_keys]
        return set(my_doll_keys)

    # 增加娃娃
    def add_model(self, item_id):
        # 娃娃的数据格式{'doll_id':40001,'exp':100,'lv':1,'state':0}
        doll = self.get_value(item_id)
        if doll is None:
            data = {'doll_id': item_id, 'exp': 0, 'lv': 1, 'state': 0}
            res = self.set_value(item_id, data)
            data['type'] = 'new'
        else:
            data = eval(doll)
            exp = 100
            data['exp'] += exp
            res = self.set_value(item_id, data)
            data['type'] = 'exp'
            data['add_exp'] = exp
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

