# -*- coding: utf-8 -*-
from lib.redis_model import HashModel
__author__ = 'du_du'


class MachineModel(HashModel):
    # 移除当前娃娃机里的娃娃蛋
    def get_model_info(self):
        data = self.get_all()
        res = dict()
        for key, value in data.items():
            res[key] = eval(value)
        return res

    def get_egg_group(self, mach_id):
        mach_keys = self.get_keys()
        mach_id = str(mach_id)
        str_keys = [str(i) for i in mach_keys if i.split('_')[0] == str(mach_id)]
        my_egg_group = set(str_keys)
        return my_egg_group

    # 移除当前娃娃机里的娃娃蛋
    def delete_egg(self, item_id):
        res = self.pop(item_id)
        return res

    def get_egg_info(self, item_id):
        res = self.get_value(item_id)
        try:
            return eval(res)
        except TypeError:
            return False

    def add_egg_list(self, data):
        res = self.set_values(data)
        return res
