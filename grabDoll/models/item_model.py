# -*- coding: utf-8 -*-
__author__ = 'dudu'
from lib.redis_model import StringModel, HashModel


class ItemModel(HashModel):
    # 增加物品
    def add_item(self, item_id, num=1):
        res = self.incr(item_id, num)
        if res is not False:
            return True
        return False

    # 移除物品
    def reduce_item(self, item_id, num=1):
        cur_ct = self.get_value(item_id)
        if cur_ct < num:
            return False
        res = self.incr(item_id, -num)
        if res == 0 or res is not False:
            return True
        return False