# -*- coding: utf-8 -*-
from grabDoll.models.user import User as UserModel
from grabDoll.models.friend_model import FriendModel
from grabDoll.models.platform_model import PlatformModel
from grabDoll.models.doll_model import DollModel
from grabDoll.models.base_model import BaseModel
import random
__author__ = 'du_du'


# 我的好友列表信息
def get_my_friend_info(uid):
    model = BaseModel(uid, FriendModel)
    data = model.hash_model.get_model_info()
    res = list()
    for f_id in data:
        p_model = PlatformModel(f_id)
        u_model = UserModel(f_id)
        item = {
            'id': f_id,
            'name': p_model.get_value('nickname').decode('utf-8'),
            'figureurl': p_model.get_value('figureurl'),
            'lv': u_model.get_value('lv')
        }
        res.append(item)
    return res


# 进入好友家
def enter_friend_home(uid, f_id):
    # 需要记录谁进来了
    print uid
    doll_model = BaseModel(f_id, DollModel)
    return doll_model.hash_model.get_model_info()


# 申请成为好友
def add_friend(uid, friend_id):
    model = BaseModel(uid, FriendModel)
    model.set_value(friend_id, {})
    return True


# 接受好友请求
def accept_friend(uid, friend_id):
    model = BaseModel(uid, FriendModel)
    model.set_value(friend_id, {})
    return True


# 拒绝好友请求
def refuse_friend(uid, friend_id):
    return True


# 移除好友
def remove_friend(uid, friend_id):
    model = BaseModel(uid, FriendModel)
    model.hash_model.delete(friend_id)
    return True


# 抢劫好友金币
def rob_money(uid, friend_id):
    u_model = BaseModel(uid, UserModel)
    f_doll_model = BaseModel(friend_id, DollModel)
    # 好友的娃娃列表
    doll_keys = f_doll_model.hash_model.get_doll_keys()
    # 默认的打劫数量
    default_rob_ct = 3
    # 需要打劫的数量
    rob_ct = min(len(doll_keys), default_rob_ct)
    # 需要打劫的娃娃列表
    doll_part = random.sample(doll_keys, rob_ct)
    gold_award = 0

    res_doll = dict()
    for doll_id in doll_part:
        doll = f_doll_model.hash_model.get_doll_info_by_id(doll_id)
        doll_gold = doll.get('gold', 0)
        gold_award += doll_gold/5
        doll['gold'] = int(doll_gold * (1 - 1.0/5))
        f_doll_model.hash_model.update_doll_info(doll_id, doll)
        res_doll[doll_id] = doll
    print res_doll
    print type(doll_keys)
    u_model.hash_model.add_gold(gold_award)

    res = {
        'gold': gold_award,
        'dolls': res_doll
    }
    return res


# 抢劫好友娃娃
def rob_doll(uid, friend_id):
    u_doll_model = BaseModel(uid, DollModel)
    f_doll_model = BaseModel(friend_id, DollModel)
    # 好友的娃娃列表
    doll_keys = f_doll_model.hash_model.get_doll_keys()
    # 默认的打劫数量
    default_rob_ct = 1
    # 需要打劫的数量
    rob_ct = min(len(doll_keys), default_rob_ct)
    # 需要打劫的娃娃列表
    doll_part = random.sample(doll_keys, rob_ct)
    doll_award = dict()
    res_doll = dict()
    for doll_id in doll_part:
        doll = f_doll_model.hash_model.get_doll_info_by_id(doll_id)
        f_doll_model.hash_model.reduce_model(doll_id)
        # 如果我有这个娃娃 增加经验
        if u_doll_model.has_key(doll_id):
            doll_award[doll_id] = u_doll_model.hash_model.add_doll_exp(doll_id, doll['exp'])
        # 如果我没有这个娃娃 增加一个
        else:
            doll_award[doll_id] = u_doll_model.hash_model.add_model(doll_id)
        res_doll[doll_id] = doll
    res = {
        'dolls': res_doll,
        'award': doll_award
    }
    return res


if __name__ == "__main__":
    # print enter_friend_home('ED57884CAA078DF9E0E08750D98CA834', 'E69014D0D63D8C50384919583C98AAAA')
    print get_my_friend_info('VIP')


