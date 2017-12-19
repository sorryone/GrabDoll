# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.mail_model import MailModel, MailTable, MailTableSerializer
import time
import collections
import hashlib
__author__ = 'du_du'


class MailAction(BaseModel):

    def __init__(self, u_id):
        self.u_id = u_id
        self.key_str = 'key_id'
        self.key_str = 'fr_id'
        self.info_str = 'info'
        self.award_str = 'award'
        super(MailAction, self).__init__(
                    u_id, MailModel, MailTable, MailTableSerializer, True)

    def get_model_info(self):
        data_list = self.get_all()
        res = sorted(data_list, key=lambda x: x['create_at'], reverse=False)
        return res

    def get_model_info_by_id(self, w_id):
        data = self.get_all({self.key_str: w_id})
        return data

    # 只有首次创建新用户初始化的时候调用
    def create_model(self, fr_id, info, award):
        key_id = hashlib.md5(self.u_id)
        data = {
            self.key_str: key_id,
        }
        return self.set_values(data, {self.key_str: key_id})



