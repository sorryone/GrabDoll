# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.book_action import HandBookAction
from grabDoll.action.hero_action import HeroAction
__author__ = 'du_du'


# 抓完娃娃后刷新当前的图鉴
def refresh_lock(uid, machine_id):
    config_model = ConfigModel('machine')
    next_book_id = machine_id + 1
    book = HandBookAction(uid)
    if book.has_key(next_book_id):
        return False
    # 判定当前关卡是否完成
    front_config = config_model.get_config_by_id(machine_id)
    if front_config:
        config_doll_group = front_config.get('itemGroup', False)
        config_exp = front_config.get('exp', 0)
        cur_exp = book.get_book_exp(machine_id)
        config_doll_group = config_doll_group.split(',')
        config_dolls = [str(i) for i in config_doll_group]
        doll_model = HeroAction(uid)
        my_doll_group = doll_model.get_doll_group()
        config_doll_group = set(config_dolls)
        # my_doll_group >= config_doll_group
        if my_doll_group.issuperset(config_doll_group) and cur_exp > config_exp:
            if book.unlock_book(next_book_id):
                return next_book_id
    return False


# 判定机器是否已经解锁
def check_book_unlock(uid, machine_id):
    book = HandBookAction(uid)
    return book.get_book_lock(machine_id)

