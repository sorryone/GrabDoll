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
        self.point_str = 'point'
        self.grab_doll_str = 'grab_doll'
        self.get_hero_str = 'get_hero'
        self.buy_vit_str = 'buy_vit'
        self.cost_gold_str = 'cost_gold'
        self.cost_diamond_str = 'cost_diamond'
        self.rob_str = 'rob'
        self.fight_str = 'fight'
        self.fight_victory_str = 'fight_victory'
        self.fight_fail_str = 'fight_fail'
        self.defend_str = 'defend'
        self.defend_victory_str = 'defend_victory'
        self.defend_fail_str = 'defend_fail'
        self.box_ct_str = 'box_ct'
        self.pve = 'pve'
        self.artifact = 'artifact'
        self.day_task_group_str = 'day_task_group'
        self.day_box_group_str = 'day_box_group'
        self.split_str = ','
        self.default_list = (self.key_str, self.point_str, self.grab_doll_str, self.get_hero_str, self.buy_vit_str,
                             self.cost_gold_str, self.rob_str, self.cost_diamond_str, self.fight_str,
                             self.fight_victory_str, self.fight_fail_str, self.defend_str, self.defend_victory_str,
                             self.defend_fail_str, self.box_ct_str, self.pve, self.artifact, self.day_task_group_str,
                             self.day_box_group_str)
        # 今天的日期
        self.day_id = int(datetime.datetime.now().strftime('%Y%m%d'))
        super(RecordAction, self).__init__(
                    u_id, RecordModel, RecordTable, RecordTableSerializer, True)

    def get_model_info(self):
        data_list = self.get_all({self.key_str: self.day_id})
        # 判定是否是新用户
        if data_list is None or len(data_list) == 0:
            # 重新获取一次
            res = self.get_empty_info()
        else:
            day_task_group = data_list.get(self.day_task_group_str, None)
            if isinstance(day_task_group, (unicode,)):
                day_task_group = day_task_group.encode('utf-8')
            if isinstance(day_task_group, (str,)):
                day_task_group = day_task_group.split(self.split_str)
            data_list[self.day_task_group_str] = day_task_group

            day_box_group = data_list.get(self.day_box_group_str, None)
            if isinstance(day_box_group, (unicode,)):
                day_box_group = day_box_group.encode('utf-8')
            if isinstance(day_box_group, (str,)):
                day_box_group = day_box_group.split(self.split_str)
            data_list[self.day_box_group_str] = day_box_group

            res = data_list
        return res

    def get_empty_info(self):
        data = {}
        for key_id in self.default_list:
            if key_id == self.key_str:
                data[key_id] = self.day_id
            else:
                if self.day_task_group_str == key_id or self.day_box_group_str == key_id:
                    data[key_id] = None
                else:
                    data[key_id] = 0
        return data

    def add_action_ct(self, action_str, ct):
        if action_str not in self.default_list:
            return False
        return self.incr(action_str, ct, {self.key_str: self.day_id})

    def update_model_info(self, data):
        task_data = data.get(self.day_task_group_str, None)
        if task_data is not None and isinstance(task_data, (list,)):
            data[self.day_task_group_str] = self.split_str.join(str(i) for i in task_data)
        box_data = data.get(self.day_box_group_str, None)
        if box_data is not None and isinstance(box_data, (list,)):
            data[self.day_box_group_str] = self.split_str.join(str(i) for i in box_data)
        return self.set_values(data, {self.key_str: self.day_id})

    def get_vit(self):
        return self.get_value(self.buy_vit_str, {self.key_str: self.day_id})

    def get_rob(self):
        return self.get_value(self.rob_str, {self.key_str: self.day_id})

    def get_fight(self):
        return self.get_value(self.fight_str, {self.key_str: self.day_id})

    def update_grab_doll(self, value):
        return self.set_value(self.grab_doll_str, value, {self.key_str: self.day_id})

    def update_vit_info(self, value):
        return self.set_value(self.buy_vit_str, value, {self.key_str: self.day_id})

    def update_rob(self, value):
        return self.set_value(self.rob_str, value, {self.key_str: self.day_id})

    def update_fight(self, value):
        return self.set_value(self.fight_str, value, {self.key_str: self.day_id})

    def update_day_task_group(self, value):
        if isinstance(value, (list,)):
            value = self.split_str.join(str(i) for i in value)
        return self.set_value(self.day_task_group_str, value, {self.key_str: self.day_id})

    def update_day_box_group(self, value):
        if isinstance(value, (list,)):
            value = self.split_str.join(str(i) for i in value)
        return self.set_value(self.day_box_group_str, value, {self.key_str: self.day_id})
