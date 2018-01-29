# -*- coding: utf-8 -*-
from lib.redis_model import StringModel, HashModel
__author__ = 'du_du'


class ConfigModel(HashModel):

    def get_model_info(self):
        data = self.get_all()
        res = dict()
        for key, value in data.items():
            res[key] = eval(value)
        return res

    def get_config_by_id(self, config_id):
        type_value = int(int(config_id)/10000)
        # 先判定抓到的娃娃蛋存不存在
        types = ("null", 'egg', 'item', 'artifact', 'doll', 'machine', 'shop', 'doll_upgrade', 'pve', 'turntable', 'task', 'user_lv', 'box')
        if len(types) >= type_value:
            res = self.get_value(config_id)
            if res:
                return eval(res)
        return False


