# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.account_model import AccountModel, AccountTable, AccountTableSerializer
import uuid
import sys
__author__ = 'du_du'


class AccountAction(BaseModel):

    def __init__(self, u_id):
        self.u_id = u_id
        self.account_id_str = 'account_id'
        self.open_id_str = 'open_id'
        self.platform_str = 'platform'
        self.account_ran_len = 5
        self.head_rate = 10000000
        super(AccountAction, self).__init__(
                    u_id, AccountModel, AccountTable, AccountTableSerializer, True)

    def get_model_last_id(self):
        res = self.get_last_id()
        return res

    def get_model_info_by_id(self, open_id, platform):
        data = self.get_user_id_by_matching({self.open_id_str: open_id, self.platform_str: platform})
        return data

    def create_model(self, open_id, platform):
        system_id = uuid.uuid3(uuid.NAMESPACE_DNS, str(open_id) + str(platform)).int
        last_id = self.get_last_id()
        head_id = max(1, last_id/self.head_rate)
        str_id_len = max(self.account_ran_len - len(str(last_id)), 1)
        str_id = str(system_id)[0:str_id_len]
        game_u_id = '%d%d%d%s' % (head_id, platform, self.get_last_id(), str_id)
        self.u_id = game_u_id
        if self.set_values({self.open_id_str: open_id, self.platform_str: platform}):
            return self.u_id
        return False


