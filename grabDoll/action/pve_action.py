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
        self.modify_at_str = 'modify_at'
        self.is_start_str = 'is_start'
        self.is_award_str = 'is_award'
        self.default_pve_id = 80001
        super(PveAction, self).__init__(
                    u_id, PveModel, PveTable, PveTableSerializer, True)

    def get_model_info(self):
        data = self.get_all()
        if isinstance(data, (list,)):
            return {self.pve_id_str: self.default_pve_id, self.is_start_str: False}
        else:
            return data

    def get_hp(self):
        res = self.get_value(self.boss_hp_str, 0)
        if isinstance(res, (int, long)):
            return res
        return 0

    def set_hp(self, value):
        res = self.set_value(self.boss_hp_str, value)
        return res




