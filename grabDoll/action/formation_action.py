# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.formation_model import FormationModel, FormationTable, FormationTableSerializer
__author__ = 'du_du'


class FormationAction(BaseModel):

    def __init__(self, u_id):
        self.u_id = u_id
        self.fight_length = 5
        self.explore_length = 5
        super(FormationAction, self).__init__(
                    u_id, FormationModel, FormationTable, FormationTableSerializer, True)

    def get_model_info(self):
        data = self.get_all()
        return data

    def get_fight_model_info(self):
        data = self.get_value('fight_formation', None)
        return data

    def get_explore_model_info(self):
        data = self.get_value('explore_formation', None)
        return data

    def set_fight_model_info(self, heroes):
        data = self.set_value('fight_formation', heroes)
        return data

    def set_explore_model_info(self, heroes):
        data = self.set_value('explore_formation', heroes)
        return data
