# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.record_model import RecordModel, RecordTable, RecordTableSerializer
import time
import collections
import datetime
__author__ = 'du_du'


class RecordAction(BaseModel):

    def __init__(self, u_id):
        self.u_id = u_id
        self.key_str = 'day_id'
        self.grab_doll_str = 'grab_doll'
        self.buy_vit_str = 'buy_vit'
        self.rob_str = 'rob'
        self.fight_str = 'fight'
        self.fight_victory_str = 'fight_victory'
        self.fight_fail_str = 'fight_fail'
        self.defend_str = 'defend'
        self.defend_victory_str = 'defend_victory'
        self.defend_fail_str = 'defend_fail'
        self.default_list = (self.key_str, self.grab_doll_str, self.buy_vit_str, self.rob_str, self.fight_str,
                             self.fight_victory_str, self.fight_fail_str, self.defend_str, self.defend_victory_str,
                             self.defend_fail_str)
        # 今天的日期
        self.day_id = datetime.datetime.now().strftime('%Y%m%d')
        super(RecordAction, self).__init__(
                    u_id, RecordModel, RecordTable, RecordTableSerializer, True)

    def get_model_info(self):
        data_list = self.get_all({self.key_str: self.day_id})
        # 判定是否是新用户
        if data_list is None:
            # 重新获取一次
            res = self.get_empty_info()
        else:
            res = data_list
        return res

    def get_empty_info(self):
        data = {}
        for key_id in self.default_list:
            if key_id == self.key_str:
                data[key_id] = self.day_id
            else:
                data[key_id] = 0
        return data

