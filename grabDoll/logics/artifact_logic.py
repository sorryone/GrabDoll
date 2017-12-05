# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.book_action import HandBookAction
from grabDoll.action.hero_action import HeroAction
__author__ = 'du_du'


# 抓完娃娃后刷新当前的图鉴
def get_artifact_info(uid):
    config_model = ConfigModel('artifact')
    return False


# 判定机器是否已经解锁
def check_book_unlock(uid, machine_id):
    pass

