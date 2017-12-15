# -*- coding: utf-8 -*-

from grabDoll.action.item_action import ItemAction
from grabDoll.action.user_action import UserAction
from grabDoll.action.machine_action import MachineAction
from grabDoll.action.hero_action import HeroAction
from grabDoll.action.hatch_action import HatchAction
from grabDoll.action.book_action import HandBookAction
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.formation_action import FormationAction
import random
__author__ = 'du_du'


def get_inventory_info(uid):
    item_action = ItemAction(uid)
    hero_action = HeroAction(uid)
    book_action = HandBookAction(uid)

    return {
        'items': item_action.get_all(),
        'dolls': hero_action.get_model_info(),
        'book': book_action.get_model_info(),
    }


def get_config_info():
    config_group = ('egg', 'item', 'artifact', 'doll', 'machine', 'shop', 'doll_upgrade', 'pve')
    config_data = dict()
    for config_name in config_group:
        config_data[config_name] = ConfigModel(config_name).get_model_info()
    return config_data


def add_item(uid, item_id):
    item_model = ItemAction(uid)
    res = item_model.add_model(item_id, 1)
    return res


def use_item(uid, item_id):
    config_id = int(item_id)
    print type(config_id)
    item_type = config_id/10000
    print('config_id', item_id, 'item_type', item_type)
    if item_type != 2:
        return False
    # 先判定抓到的娃娃蛋存不存在
    del_res = reduce_item(uid, item_id)
    # 存在的话删除掉
    if del_res:
        config_model = ConfigModel('item')
        config_info = config_model.get_config_by_id(item_id)
        fun_dict = {
            'normal': use_normal,
            'box': use_heal,
            'heal': use_heal,
        }
        return fun_dict.get(config_info['iType'])(uid, config_info)
    print("item  is not exits")
    return False


def use_normal(uid, config_info=None):
    res = {}
    user = UserAction(uid)
    ct = 1
    user.add_gold(ct)
    res['gold'] = ct
    return res


# 使用宝箱
def use_box(uid, config_info):
    # 奖励
    awards = get_award(config_info)
    item_model = ItemAction(uid)
    doll_model = HeroAction(uid)
    hatch_action = HatchAction(uid)
    user = UserAction(uid)
    res = dict()
    for a_id, ct in awards.iteritems():
        # 如果是金币添加金币
        if a_id == "gold":
            user.add_gold(ct)
            res[a_id] = ct
        # 如果是钻石添加钻石
        elif a_id == "diamond":
            user.add_diamond(ct)
            res[a_id] = ct
        # 经验
        elif a_id == "exp":
            user.add_gold(ct)
            res[a_id] = ct
        # 如果是道具添加道具
        elif int(a_id) / 10000 == 2:
            if item_model.add_model(a_id, ct):
                res[a_id] = ct
        elif int(a_id) / 10000 == 3:
            hatch_action.add_model(a_id)
        elif int(a_id) / 10000 == 4:
            res['doll'] = doll_model.add_model(a_id)
        else:
            pass
    return res


# 添加一堆的奖励
def add_awards(uid,awards):
    item_model = ItemAction(uid)
    doll_model = HeroAction(uid)
    hatch_action = HatchAction(uid)
    user = UserAction(uid)
    res = dict()
    for a_id, ct in awards.iteritems():
        # 如果是金币添加金币
        if a_id == "gold":
            user.add_gold(ct)
            res[a_id] = ct
        # 如果是钻石添加钻石
        elif a_id == "diamond":
            user.add_diamond(ct)
            res[a_id] = ct
        # 经验
        elif a_id == "exp":
            user.add_gold(ct)
            res[a_id] = ct
        # 如果是道具添加道具
        elif int(a_id) / 10000 == 2:
            if item_model.add_model(a_id, ct):
                res[a_id] = ct
        elif int(a_id) / 10000 == 3:
            hatch_action.add_model(a_id)
        elif int(a_id) / 10000 == 4:
            res['doll'] = doll_model.add_model(a_id)
        else:
            pass
    return res


# 治疗书的使用
def use_heal(uid, config_info=None):
    formation_action = FormationAction(uid)
    formation_info = formation_action.get_model_info()
    if formation_info.get(formation_action.fight_state_str) != formation_action.state_injured:
        return False
    res = formation_action.set_normal()
    return {'heal': res}


def reduce_item(uid, item_id):
    item_model = ItemAction(uid)
    return item_model.remove_model(item_id, 1)


def reduce_egg(uid, item_id):
    action = MachineAction(uid)
    return action.delete_egg(item_id)


def reduce_hatch(uid, item_id):
    hatch_action = HatchAction(uid)
    return hatch_action.remove_model(item_id)


# 查看奖励
def get_award(config_info):
    award = config_info.get('award', dict())
    if type(award) is not dict:
        award = award.encode('utf-8')
        award = eval(award)
    award_type = config_info.get('xType', 0)    # 0表示随机  1 表示必出
    data = dict()
    if award_type == 0:
        keys = award.keys()
        select_key = random.choice(keys)
        select_value = award[select_key]
        if type(select_value) is list:
            if select_key == 'gold' or select_key == 'diamond':
                data[select_key] = random.randint(select_value[0], select_value[1])
            else:
                data[select_key] = random.choice(select_value)
        else:
            data[select_key] = select_value
    else:
        for key, value in award.items():
            if type(value) is list:
                if key == 'gold' or key == 'diamond':
                    data[key] = random.randint(value[0], value[1])
                else:
                    data[key] = random.choice(value)
            else:
                data[key] = value
    print('get_award', data)
    return data


def gacha_speed_up(uid, item_id):
    config_id = int(item_id.split("_")[0])
    item_type = config_id / 10000
    if item_type is not 2 or reduce_item(uid, config_id) is not True:
        return 1, "使用失败"
    config_model = ConfigModel("config")
    config_info = config_model.get_config_by_id(config_id)
    if config_info and config_info.get('type', 0) == "speed":
        exp = config_info.get('exp', 0)
        return 0, exp
    else:
        return 1, "无效的道具"


if __name__ == "__main__":
    print use_item('ED57884CAA078DF9E0E08750D98CA834', 20006)
    # print get_award(20006)
