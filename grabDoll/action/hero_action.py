# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.doll_model import DollModel, DollTable, DollTableSerializer
__author__ = 'du_du'


class HeroAction(BaseModel):

    def __init__(self, u_id):
        self.u_id = u_id
        super(HeroAction, self).__init__(
                    u_id, DollModel, DollTable, DollTableSerializer, False)

    def get_model_info(self):
        data = self.get_all()
        res = dict()
        for key, value in data.items():
            res[key] = eval(value)
        return res

    def get_doll_keys(self):
        return self.get_keys()

    def get_doll_group(self):
        doll_keys = self.get_keys()
        my_doll_keys = [str(i) for i in doll_keys]
        return set(my_doll_keys)

    def get_doll_info_by_id(self, item_id):
        data = self.get_value(item_id)
        if data is None:
            return []
        else:
            return eval(data)

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

    # 增加娃娃经验
    def add_doll_exp(self, doll_id, exp):
        doll = self.get_doll_info_by_id(doll_id)
        if doll.has_key('exp'):
            doll['exp'] += exp
            return doll
        return False

    # 修改娃娃的数据
    def update_doll_info(self, doll_id, data):
        res = self.set_value(doll_id, data)
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