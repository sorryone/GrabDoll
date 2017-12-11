# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.pve_model import PveModel, PveTable, PveTableSerializer
import time
__author__ = 'du_du'


class PveAction(BaseModel):

    def __init__(self, u_id):
        self.u_id = u_id
        self.pve_id_str = 'pve_id'
        self.boss_hp_str = 'boss_hp'
        self.fight_refresh_time_str = 'fight_refresh_time'
        super(PveAction, self).__init__(
                    u_id, PveModel, PveTable, PveTableSerializer, True)

    def get_model_info(self):
        data = self.get_all()
        if isinstance(data, (list,)):
            return {}
        else:
            return {self.pve_id_str: 80001}

    def get_hp(self):
        res = self.get_value(self.boss_hp_str, 0)
        if isinstance(res, (int, long)):
            return res
        return 0

    def set_hp(self, value):
        res = self.set_value(self.boss_hp_str, value)
        return res




