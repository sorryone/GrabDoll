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
        super(FormationAction, self).__init__(
                    u_id, FormationModel, FormationTable, FormationTableSerializer, True)

    def get_model_info(self):
        data = self.get_all()
        return data

    def get_income(self):
        return self.get_value('income', 0)

    def get_fight_atk(self):
        return self.get_value('fight_atk', 0)

    def get_fight_model_info(self):
        data = self.get_value('fight_formation', None)
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
        data = self.get_value('explore_formation', None)
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

    def set_fight_model_info(self, heroes, fight_atk):
        if isinstance(heroes, (list,)) and len(heroes) == self.fight_length:
            data = self.split_str.join(str(i) for i in heroes)
            res = self.set_values({'fight_formation': data.encode('utf-8'), 'fight_atk': fight_atk})
            return res
        return False

    def set_explore_model_info(self, heroes):
        if isinstance(heroes, (list,)) and len(heroes) == self.fight_length:
            data = self.split_str.join(str(i) for i in heroes)
            res = self.set_value('explore_formation', data.encode('utf-8'))
            return res
        return False
