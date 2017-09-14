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
        res['uid'] = data['uid']
        res['name'] = data['name']
        res['gold'] = data['gold']
        res['diamond'] = data['diamond']
        res['exp'] = data['exp']
        res['lv'] = data['lv']
        res['machineLv'] = data['machineLv']
        res['curMachineId'] = data['curMachineId']
        res['maxUnLockLv'] = data['maxUnLockLv']
        return res
