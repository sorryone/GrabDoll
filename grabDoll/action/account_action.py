# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.account_model import AccountModel, AccountTable, AccountTableSerializer
__author__ = 'du_du'


class AccountAction(BaseModel):

    def __init__(self, u_id):
        self.u_id = u_id
        self.account_id_str = 'account_id'
        self.open_id_str = 'open_id'
        self.platform_str = 'platform'
        super(AccountAction, self).__init__(
                    u_id, AccountModel, AccountTable, AccountTableSerializer, True)

    def get_model_last_id(self):
        res = self.get_last_id()
        return res

    def get_model_info_by_id(self, open_id, platform):
        data = self.get_all_by_userlist({self.open_id_str: open_id, self.platform_str: platform})
        return data


