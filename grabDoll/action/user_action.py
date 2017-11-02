# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.user import User, UserTable, UserTableSerializer
__author__ = 'du_du'


class UserAction(BaseModel):
    def __init__(self, u_id):
        self.u_id = u_id
        super(UserAction, self).__init__(
                    u_id, User, UserTable, UserTableSerializer, True)

    def add_gold(self, ct):
        self.incr("gold", ct)
        return True

    def reduce_gold(self, ct):
        return self.incr(-ct)

    def add_diamond(self, ct):
        self.incr("diamond", ct)
        return True

    def add_exp(self, ct):
        self.incr("exp", ct)
        return True

    def add_vit(self, ct):
        self.incr("vit", ct)
        return True

    def get_model_info(self):
        data = self.get_all()
        if not data:
            data = {
                'gold': 1000,
                'diamond': 100,
                'uid': self.u_id,
                'exp': 0,
                'lv': 1,
            }
            return self.set_values(data)
        res = {}
        key_info = ('uid', 'name', 'gold', 'diamond', 'exp', 'vit', 'lv')
        for key in key_info:
            if key in data:
                res[key] = data[key]
            else:
                res[key] = 0
        return res
