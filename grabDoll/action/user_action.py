# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.user import User, UserTable, UserTableSerializer
__author__ = 'du_du'


class UserAction(BaseModel):
    def __init__(self, u_id):
        self.u_id = u_id
        super(UserAction, self).__init__(
                    u_id, User, UserTable, UserTableSerializer, True)

    def get_gold(self):
        return self.get_value("gold")

    def get_diamond(self):
        return self.get_value("diamond")

    def add_gold(self, ct):
        self.incr("gold", ct)
        return True

    def reduce_gold(self, ct):
        return self.incr("gold", -ct)

    def add_diamond(self, ct):
        self.incr("diamond", ct)
        return True

    def reduce_diamond(self, ct):
        self.incr("diamond", -ct)
        return True

    def add_exp(self, ct):
        self.incr("exp", ct)
        return True

    def add_vit(self, ct):
        self.incr("vit", ct)
        return True

    def reduce_vit(self, ct):
        self.incr("vit", -ct)
        return True

    def get_model_info(self):
        data = self.get_all()
        res = {}
        key_info = ('uid', 'name', 'gold', 'diamond', 'exp', 'vit', 'lv')
        if len(data) > 0:
            for key in key_info:
                if key in data[0]:
                    res[key] = data[0][key]
                else:
                    res[key] = 0
        return res

    # 创建新用户
    def create_model(self):
        data = {
            'gold': 1000,
            'diamond': 100,
            'uid': self.u_id,
            'exp': 0,
            'lv': 1,
        }
        return self.set_values(data)
