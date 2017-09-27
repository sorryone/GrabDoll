# -*- coding: utf-8 -*-
from lib.redis_model import StringModel, HashModel
import time
__author__ = 'du_du'


class NoteModel(HashModel):

    def get_model_info(self):
        return self.get_all()

    def get_cur_machine(self):
        res = self.get_value('cur_machine')
        if type(res) is str:
            res = int(res)
        return res

    def set_cur_machine(self, machine_id):
        res = self.set_value('cur_machine', machine_id)
        return res

    # 获取最近一次刷新娃娃蛋的时间
    def get_egg_refresh_time(self):
        res = self.get_value('egg_refresh')
        if res is None:
            res = 0
        elif type(res) is str:
            res = float(res)
        return res

    def get_machine_create_time(self, machine_id):
        res = self.get_value('egg_refresh' + str(machine_id))
        if res is None:
            res = 0
        elif type(res) is str:
            res = float(res)
        return res

    def set_machine_create_time(self, machine_id):
        time_str = time.time()
        res = self.set_value('egg_refresh' + str(machine_id), time_str)
        return res
