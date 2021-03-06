# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.user import User, UserTable, UserTableSerializer
import time
__author__ = 'du_du'


class UserAction(BaseModel):
    def __init__(self, u_id):
        self.u_id = u_id
        self.gold_str = 'gold'
        self.diamond_str = 'diamond'
        self.vit_str = 'vit'
        self.lv_str = 'lv'
        self.exp_str = 'exp'
        self.max_vit_value = 100
        self.private_property = ('uid', 'name', 'gold', 'diamond', 'exp', 'vit', self.lv_str, self.exp_str)
        super(UserAction, self).__init__(
                    u_id, User, UserTable, UserTableSerializer, True)

    def check_exist(self):
        data = self.get_all()
        if len(data) == 0:
            return False
        return True

    def get_gold(self):
        return self.get_value("gold")

    def get_diamond(self):
        return self.get_value("diamond")

    def get_vit(self):
        return self.get_value("vit")

    def reset_vit(self):
        return self.set_value("vit", self.max_vit_value)

    def add_gold(self, ct):
        self.incr("gold", ct)
        return True

    def reduce_gold(self, ct):
        cur_value = self.get_gold()
        if cur_value < ct:
            return False
        res = self.incr("gold", -ct)
        if res >= 0:
            self.send_task_update('cost_gold', ct)
        return res

    def add_diamond(self, ct):
        self.incr("diamond", ct)
        return True

    def reduce_diamond(self, ct):
        cur_value = self.get_diamond()
        if cur_value < ct:
            return False
        res = self.incr("diamond", -ct)
        if res >= 0:
            self.send_task_update('cost_diamond', ct)
        return res

    def send_task_update(self, *data):
        from grabDoll.logics import record_logic
        record_logic.add_record(self.u_id, *data)

    def add_exp(self, ct):
        self.incr("exp", ct)
        return True

    def add_vit(self, ct):
        self.incr("vit", ct)
        return True

    def reduce_vit(self, ct):
        cur_value = self.get_vit()
        if cur_value < ct:
            return False
        self.incr("vit", -ct)
        return True

    def get_model_info(self):
        data = self.get_all()
        res = {}
        if len(data) == 0:
            data = self.create_model()
        key_info = ('uid', 'name', 'gold', 'diamond', 'exp', 'vit', 'lv')
        for key in key_info:
            if key in data:
                res[key] = data[key]
            else:
                res[key] = 0
        return res

    def get_private_info(self):
        data = self.get_all()
        res = {}
        if len(data) == 0:
            data = self.create_model()
        key_info = ('uid', 'name', 'gold', 'diamond', 'exp', 'vit', 'lv')
        for key in key_info:
            if key in data:
                res[key] = data[key]
            else:
                res[key] = 0
        return res

    def update_info(self, info):
        return self.set_values(info)

    # 创建新用户
    def create_model(self):
        data = {
            'gold': 1000,
            'diamond': 100,
            'uid': self.u_id,
            'exp': 0,
            'vit': self.max_vit_value,
            'lv': 1,
        }
        if self.set_values(data):
            return data
        return {}

    def test_model_info(self):
        start_time = time.time()
        data = self.get_all()
        print data
        return time.time() - start_time
