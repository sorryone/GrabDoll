# -*- coding: utf-8 -*-
from lib.redis_model import HashModel
import time
__author__ = 'du_du'


class NoteModel(HashModel):

    def __init__(self, uid):
        self.login_time_str = 'login_time'
        self.buy_vit_ct_str = 'buy_vit_ct'
        HashModel.__init__(self, uid)

    def get_model_info(self):
        return self.get_all()

    def get_cur_machine(self):
        res = self.get_value('cur_machine')
        if type(res) is str:
            res = int(res)
        return res

    def get_login_time(self):
        res = self.get_value(self.login_time_str)
        if res is None:
            res = 0
        if type(res) is str:
            res = float(res)
        return res

    def set_login_time(self):
        res = self.set_value(self.login_time_str, time.time())
        if res == 0 or res is not False:
            return True
        return False

    def get_buy_vit_ct(self):
        res = self.get_value(self.buy_vit_ct_str)
        if res is None:
            res = 0
        if type(res) is str:
            res = int(res)
        return res

    def add_buy_vit_ct(self):
        return self.incr(self.buy_vit_ct_str)

    def reset_buy_vit_ct(self):
        return self.set_value(self.buy_vit_ct_str, 0)

    def set_cur_machine(self, machine_id):
        res = self.set_value('cur_machine', machine_id)
        if res == 0 or res is not False:
            return True
        return False

    def get_machine_create_time(self, machine_id):
        res = self.get_value('machine_refresh_' + str(machine_id))
        if res is None:
            res = 0
        elif type(res) is str:
            res = float(res)
        return res

    def set_machine_create_time(self, machine_id):
        time_str = time.time()
        res = self.set_value('machine_refresh_' + str(machine_id), time_str)
        return res

    def get_vit_refresh_time(self):
        res = self.get_value('vit_refresh_time')
        if res is None:
            res = 0
        if type(res) is str:
            res = float(res)
        return res

    def set_vit_refresh_time(self):
        res = self.set_value('vit_refresh_time', time.time())
        if res == 0 or res is not False:
            return True
        return False

    def get_redis(self):
        self.get_client()
