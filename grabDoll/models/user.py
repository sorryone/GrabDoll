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
