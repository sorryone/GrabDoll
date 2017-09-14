# -*- coding: utf-8 -*-
from lib.redis_model import StringModel, HashModel
__author__ = 'du_du'


class MachineModel(HashModel):
    # 移除当前娃娃机里的娃娃蛋
    def get_model_info(self):
        data = self.get_all()
        res = dict()
        for key, value in data:
            res[key] = eval(value)
        return res

    # 移除当前娃娃机里的娃娃蛋
    def delete_egg(self, item_id):
        res = self.pop(item_id)
        return res

    def add_egg(self, data):
        res = self.set_values(data)
        return res

    def add_egg_list(self, data):
        res = self.set_values(data)
        return res
