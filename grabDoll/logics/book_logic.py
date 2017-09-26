# -*- coding: utf-8 -*-
from grabDoll.models.doll_model import DollModel
from grabDoll.models.config_model import ConfigModel
from grabDoll.models.handbook_model import HandBookModel

__author__ = 'du_du'


# 抓完娃娃后刷新当前的图鉴
def refresh_lock(uid, machine_id):
    config_model = ConfigModel('machine')
    # 判定当前关卡是否完成
    front_config = config_model.get_config_by_id(machine_id)
    if front_config:
        config_doll_group = front_config.get('itemGroup', False)
        config_exp = front_config.get('exp', 0)
        book = HandBookModel(uid)
        cur_exp = book.get_book_exp(front_config)
        config_doll_group = config_doll_group.split(',')
        config_dolls = [str(i) for i in config_doll_group]
        doll_model = DollModel(uid)
        doll_keys = doll_model.get_keys()
        # doll_keys.extend([40009, 40012, 40003, 40004])
        my_doll_keys = [str(i) for i in doll_keys]
        my_doll_group = set(my_doll_keys)
        config_doll_group = set(config_dolls)
        # my_doll_group >= config_doll_group
        if my_doll_group.issuperset(config_doll_group) and cur_exp > config_exp:
            book = HandBookModel(uid)
            next_book_id = machine_id + 1
            if book.get_book_lock(next_book_id) is False:
                return book.unlock_book(next_book_id)
    return False


# 判定机器是否已经解锁
def check_book_unlock(uid, machine_id):
    book = HandBookModel(uid)
    return book.get_book_lock(machine_id)

