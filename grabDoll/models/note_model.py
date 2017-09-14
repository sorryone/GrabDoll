# -*- coding: utf-8 -*-
from lib.redis_model import StringModel, HashModel
__author__ = 'du_du'


class NoteModel(HashModel):

    # 设置刷新娃娃蛋的时间
    def set_egg_refresh_time(self, time_str):
        res = self.set_value('egg_refresh', time_str)
        return res

    # 获取最近一次刷新娃娃蛋的时间
    def get_egg_refresh_time(self):
        res = self.get_value('egg_refresh')
        if res is None:
            res = 0
        elif type(res) is str:
            res = float(str)
        return res
