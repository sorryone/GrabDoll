# -*- coding: utf-8 -*-
__author__ = 'dudu'
from lib.redis_model import StringModel, HashModel


class MachineModel(HashModel):
    # 移除当前娃娃机里的娃娃蛋
    def get_machine_info(self):
        return self.get_all()

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