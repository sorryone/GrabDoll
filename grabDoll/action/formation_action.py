# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.formation_model import FormationModel, FormationTable, FormationTableSerializer
import time
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
        self.capacity_update_at_str = 'capacity_update_at'
        self.income_str = 'income'
        self.fight_state_str = 'fight_state'
        self.fight_atk_str = 'fight_atk'
        # 进攻对手的次数
        self.fight_ct_str = 'fight_ct'
        # 打劫别人的次数
        self.rob_ct_str = 'rob_ct'
        # 被打劫的次数
        self.catch_ct_str = 'catch_ct'
        # 防守次数
        self.defend_ct_str = 'defend_ct'
        self.defend_refresh_time_str = 'defend_refresh_time'
        self.rob_refresh_time_str = 'rob_refresh_time'
        self.catch_refresh_time_str = 'catch_refresh_time'
        self.fight_refresh_time_str = 'fight_refresh_time'
        self.fight_type = 1
        self.capacity_type = 0
        self.state_normal = 0
        self.state_injured = 1
        super(FormationAction, self).__init__(
                    u_id, FormationModel, FormationTable, FormationTableSerializer, True)

    def get_model_info(self):
        data = self.get_all()
        # 判定是否是新用户
        if len(data) == 0:
            self.create_model()
            # 重新获取一次
            data = self.get_all()
        data[self.fight_formation_str] = self.change_list_by_ct(data[self.fight_formation_str], self.fight_length)
        data[self.explore_formation_str] = self.change_list_by_ct(data[self.explore_formation_str], self.explore_length)
        return data

    def create_model(self):
        self.set_value(self.income_str, 0)

    def get_private_info(self):
        data = self.get_all()
        keys_group = (self.income_str, self.fight_atk_str)
        return data

    def get_income(self):
        res = self.get_value(self.income_str, 0)
        if isinstance(res, (int, long)):
            return res
        return 0

    def set_income(self, value):
        res = self.set_value(self.income_str, value)
        return res

    def get_fight_atk(self):
        res = self.get_value(self.fight_atk_str, 0)
        if isinstance(res, (int, long)):
            return res
        return 0

    def get_capacity(self):
        res = self.get_value(self.capacity_str, 0)
        if isinstance(res, (int, long)):
            return res
        return 0

    def get_fight_model_info(self):
        data = self.get_value(self.fight_formation_str, None)
        return self.change_list_by_ct(data, self.fight_length)

    def get_explore_model_info(self):
        data = self.get_value(self.explore_formation_str, None)
        return self.change_list_by_ct(data, self.explore_length)

    def change_list_by_ct(self, data, ct):
        res = []
        if isinstance(data, (unicode,)):
            data = data.encode('utf-8')
        if isinstance(data, (str,)):
            res = data.split(self.split_str)
        fill_ct = ct - len(res)
        if fill_ct > 0:
            res.extend([''] * fill_ct)
        return res

    def set_normal(self):
        res = {
            self.fight_state_str: self.state_normal,
            self.capacity_update_at_str: int(time.time())
        }
        return self.set_values(res)

    def set_injured(self):
        return self.set_value(self.fight_state_str, self.state_injured)

    def set_model_info(self, data):
        fight_formation = data.get(self.fight_formation_str)
        explore_formation = data.get(self.explore_formation_str)
        if isinstance(fight_formation, (list,)) and len(fight_formation) == self.fight_length:
            data[self.fight_formation_str] = self.split_str.join(str(i) for i in fight_formation)
        if isinstance(explore_formation, (list,)) and len(explore_formation) == self.fight_length:
            data[self.explore_formation_str] = self.split_str.join(str(i) for i in explore_formation)
        return self.set_values(data)

