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
        self.mType_str = 'mType'
        self.info_str = 'info'
        self.award_str = 'award'
        self.read_str = 'read'
        self.can_delete_str = 'can_delete'
        self.create_at_str = 'create_at'
        self.is_delete_str = 'is_delete'
        self.lv_up_type = 1
        self.invite_type = 2
        self.friend_type = 3
        self.key_info = ('u_id', self.key_str, self.fr_id_str, self.mType_str, self.info_str, self.award_str, self.create_at_str,
                         self.read_str, self.can_delete_str)
        super(MailAction, self).__init__(
                    u_id, MailModel, MailTable, MailTableSerializer, True)

    def get_model_info(self):
        data_list = self.get_all({self.is_delete_str: False})
        return self.get_mail_list_by_filter(data_list)

    def get_mails_by_type(self, m_type, is_read):
        data_list = self.get_all({self.mType_str: m_type, self.read_str: is_read, self.is_delete_str: False})
        return self.get_mail_list_by_filter(data_list)

    def get_can_delete_mails(self):
        data_list = self.get_all({self.can_delete_str: True, self.is_delete_str: False})
        return self.get_mail_list_by_filter(data_list)

    def remove_scrap_mails(self):
        data_list = self.update_values({self.is_delete_str: True}, {self.can_delete_str: True, self.is_delete_str: False})
        return self.get_mail_list_by_filter(data_list)

    def get_need_award_mails(self):
        data_list = self.get_all({self.read_str: False, self.is_delete_str: False})
        return self.get_mail_list_by_filter(data_list)

    def mark_read_group(self):
        data = {
            self.read_str: True,
            self.can_delete_str: True,
        }
        return self.update_values(data, {self.read_str: False, self.can_delete_str: False})

    def get_model_info_by_id(self, w_id):
        data = self.get_all({self.key_str: w_id, self.is_delete_str: False})
        return data

    def get_mail_list_by_filter(self, data_list):
        res = []
        if isinstance(data_list, (dict, collections.OrderedDict)):
            res_item = self.filter_data(data_list)
            res.append(res_item)
        else:
            # 如果是数组
            for index, data in enumerate(data_list):
                res_item = self.filter_data(data)
                res.append(res_item)
        return res

    def filter_data(self, data):
        res_item = dict()
        for key in self.key_info:
            if key in data:
                res_item[key] = data[key]
        return res_item

    # 升级奖励
    def add_lv_up_award(self, award):
        key_id = self.get_key_id()
        data = {
            self.key_str: key_id,
            self.mType_str: self.lv_up_type,
            self.award_str: award,
        }
        return self.set_values(data, {self.key_str: key_id})

    # 邀请好友的奖励
    def add_invite_award(self, award):
        key_id = self.get_key_id()
        data = {
            self.key_str: key_id,
            self.mType_str: self.invite_type,
            self.award_str: award,
        }
        return self.set_values(data, {self.key_str: key_id})

    # 战斗日志
    def add_fight_message(self, fight_u_id):
        key_id = self.get_key_id()
        data = {
            self.key_str: key_id,
            self.mType_str: self.friend_type,
            self.fr_id_str: fight_u_id,
            self.can_delete_str: True,
        }
        return self.set_values(data, {self.key_str: key_id, self.can_delete_str: True})

    def mark_read(self, key_id):
        data = {
            self.read_str: True,
            self.can_delete_str: True,
        }
        return self.set_values(data, {self.key_str: key_id})

    def get_key_id(self):
        return hashlib.md5(self.u_id + str(time.time())).hexdigest()

