# -*- coding: utf-8 -*-
from lib.redis_model import HashModel
__author__ = 'maxijie'


class BaseModel(object):
    def has_key(self, key):
        pass

    def get_keys(self):
        pass

    def get_value(self, key, default=None):
        pass

    def get_values(self, key_list):
        pass

    def get_all(self):
        pass

    def set_value(self, key, value):
        pass

    def set_values(self, key, value_list):
        pass

    def incr(self, key, amount=1):
        pass

    def remove(self, key):
        pass
