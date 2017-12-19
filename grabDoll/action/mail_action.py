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
        self.fr_id_str = 'fr_id'
        self.mType = 'mType'
        self.info_str = 'info'
        self.award_str = 'award'
        self.lv_up_type = 1
        self.invite_type = 2
        self.friend_type = 3
        super(MailAction, self).__init__(
                    u_id, MailModel, MailTable, MailTableSerializer, True)

    def get_model_info(self):
        data_list = self.get_all()
        res = sorted(data_list, key=lambda x: x['create_at'], reverse=False)
        return res

    def get_model_info_by_id(self, w_id):
        data = self.get_all({self.key_str: w_id})
        return data

    # 升级奖励
    def add_lv_up_award(self, award):
        key_id = self.get_key_id()
        data = {
            self.key_str: key_id,
            self.mType: self.lv_up_type,
            self.award_str: award,
        }
        return self.set_values(data, {self.key_str: key_id})

    # 邀请好友的奖励
    def add_invite_award(self, award):
        key_id = self.get_key_id()
        data = {
            self.key_str: key_id,
            self.mType: self.invite_type,
            self.award_str: award,
        }
        return self.set_values(data, {self.key_str: key_id})

    # 战斗日志
    def add_fight_message(self, fight_u_id):
        key_id = self.get_key_id()
        data = {
            self.key_str: key_id,
            self.mType: self.friend_type,
            self.fr_id_str: fight_u_id,
        }
        return self.set_values(data, {self.key_str: key_id})

    def get_key_id(self):
        return hashlib.md5(self.u_id + time.time())