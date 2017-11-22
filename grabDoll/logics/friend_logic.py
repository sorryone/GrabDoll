# -*- coding: utf-8 -*-
from grabDoll.action.user_action import UserAction
from grabDoll.action.friend_action import FriendAction
from grabDoll.action.platform_action import PlatformAction
from grabDoll.action.hero_action import HeroAction
import random
__author__ = 'du_du'


# 我的好友列表信息
def get_my_friend_info(uid):
    model = FriendAction(uid)
    data = model.get_model_info()
    res = list()
    for f_id in data:
        p_model = PlatformAction(f_id)
        u_model = UserAction(f_id)
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
    hero_action = HeroAction(f_id)
    res = {
        'id': f_id,
        'heroes': hero_action.get_model_info(),
        'money': 1000,
    }
    return res


# 申请成为好友
def add_friend(uid, friend_id):
    friend_action = FriendAction(uid)
    friend_action.set_value(friend_id, {})
    return True


# 接受好友请求
def accept_friend(uid, friend_id):
    model = FriendAction(uid)
    model.set_value(friend_id, {})
    return True


# 拒绝好友请求
def refuse_friend(uid, friend_id):
    return True


# 移除好友
def remove_friend(uid, friend_id):
    model = FriendAction(uid)
    model.delete(friend_id)
    return True


# 抢劫好友金币
def rob_money(uid, friend_id):
    u_model = UserAction(uid)
    f_doll_model = HeroAction(friend_id)
    # 好友的娃娃列表
    doll_keys = f_doll_model.get_doll_keys()
    # 默认的打劫数量
    default_rob_ct = 3
    # 需要打劫的数量
    rob_ct = min(len(doll_keys), default_rob_ct)
    # 需要打劫的娃娃列表
    doll_part = random.sample(doll_keys, rob_ct)
    gold_award = 0
    res_doll = {}
    for doll_id in doll_part:
        doll = f_doll_model.get_doll_info_by_id(doll_id)
        doll_gold = doll.get('gold', 0)
        gold_award += doll_gold/5
        doll['gold'] = int(doll_gold * (1 - 1.0/5))
        f_doll_model.update_doll_info(doll_id, doll)
        res_doll[doll_id] = doll
    print res_doll
    print type(doll_keys)
    u_model.add_gold(gold_award)

    res = {
        'gold': gold_award,
        'dolls': res_doll
    }
    return res


# 抢劫好友娃娃
def rob_doll(uid, friend_id):
    u_doll_model = HeroAction(uid)
    f_doll_model = HeroAction(friend_id)
    # 好友的娃娃列表
    doll_keys = f_doll_model.get_doll_keys()
    # 默认的打劫数量
    default_rob_ct = 1
    # 需要打劫的数量
    rob_ct = min(len(doll_keys), default_rob_ct)
    # 需要打劫的娃娃列表
    doll_part = random.sample(doll_keys, rob_ct)
    doll_award = dict()
    res_doll = dict()
    for doll_id in doll_part:
        doll = f_doll_model.get_doll_info_by_id(doll_id)
        f_doll_model.reduce_model(doll_id)
        # 如果我有这个娃娃 增加经验
        if u_doll_model.has_key(doll_id):
            doll_award[doll_id] = u_doll_model.add_doll_exp(doll_id, doll['exp'])
        # 如果我没有这个娃娃 增加一个
        else:
            doll_award[doll_id] = u_doll_model.add_model(doll_id)
        res_doll[doll_id] = doll
    res = {
        'dolls': res_doll,
        'award': doll_award
    }
    return res


if __name__ == "__main__":
    # print enter_friend_home('ED57884CAA078DF9E0E08750D98CA834', 'E69014D0D63D8C50384919583C98AAAA')
    print get_my_friend_info('VIP')


