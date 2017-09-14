# -*- coding: utf-8 -*-
__author__ = 'maxijie'
from lib.redis_model import StringModel, HashModel


class User(HashModel):
    def add_gold(self, ct):
        self.incr("gold", ct)
        return True

    def add_diamond(self, ct):
        self.incr("diamond", ct)
        return True

    def add_exp(self, ct):
        self.incr("exp", ct)
        return True

    def get_model_info(self):
        data = self.get_all()
        res = dict()
        key_info = ('uid', 'name', 'gold', 'diamond', 'exp', 'lv', 'machineLv', 'curMachineId', 'maxUnLockLv')
        for key in key_info:
            if type(data) == dict and key in data:
                res[key] = data[key]
            else:
                res[key] = 0
        return res
