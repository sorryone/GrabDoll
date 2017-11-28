# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.formation_model import FormationModel, FormationTable, FormationTableSerializer
__author__ = 'du_du'


class FormationAction(BaseModel):

    def __init__(self, u_id):
        self.u_id = u_id
        self.fight_length = 5
        self.explore_length = 5
        self.split_str = ','
        self.fight_formation_str = 'fight_formation'
        self.explore_formation_str = 'explore_formation'
        self.capacity_str = 'capacity'
        self.income_str = 'income'
        self.fight_atk_str = 'fight_atk'
        self.fight_type = 1
        self.capacity_type = 0
        super(FormationAction, self).__init__(
                    u_id, FormationModel, FormationTable, FormationTableSerializer, True)

    def get_model_info(self):
        data = self.get_all()
        return data

    def get_income(self):
        res = self.get_value(self.income_str, 0)
        if isinstance(res, (dict, list)):
            return 0
        return res

    def set_income(self, value):
        res = self.set_value(self.income_str, value)
        return res

    def get_fight_atk(self):
        res = self.get_value(self.fight_atk_str, 0)
        if isinstance(res, (dict, list)):
            return 0
        return res

    def get_capacity(self):
        res = self.get_value(self.capacity_str, 0)
        if isinstance(res, (dict, list)):
            return 0
        return res

    def get_fight_model_info(self):
        data = self.get_value(self.fight_formation_str, None)
        res = []
        if isinstance(data, (unicode,)):
            print('start utf-8')
            data = data.encode('utf-8')
        if isinstance(data, (str,)):
            res = data.split(self.split_str)
        fill_ct = self.fight_length - len(res)
        if fill_ct > 0:
            res.extend([''] * fill_ct)
        return res

    def get_explore_model_info(self):
        data = self.get_value(self.explore_formation_str, None)
        res = []
        if isinstance(data, (unicode,)):
            print('start utf-8')
            data = data.encode('utf-8')
        if isinstance(data, (str,)):
            res = data.split(self.split_str)
            print(res)
        fill_ct = self.explore_length - len(res)
        if fill_ct > 0:
            res.extend([''] * fill_ct)
        print(fill_ct)
        return res

    def set_model_info(self, data):
        fight_formation = data.get(self.fight_formation_str)
        explore_formation = data.get(self.explore_formation_str)
        if isinstance(fight_formation, (list,)) and len(fight_formation) == self.fight_length:
            data[self.fight_formation_str] = self.split_str.join(str(i) for i in fight_formation)
        if isinstance(explore_formation, (list,)) and len(explore_formation) == self.fight_length:
            data[self.explore_formation_str] = self.split_str.join(str(i) for i in explore_formation)
        return self.set_values(data)

