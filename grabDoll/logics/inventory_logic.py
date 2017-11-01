# -*- coding: utf-8 -*-

from grabDoll.action.item_action import ItemAction
from grabDoll.action.user_action import UserAction
from grabDoll.models.machine_model import MachineModel
from grabDoll.action.hero_action import HeroAction
from grabDoll.models.gacha_model import GachaModel
from grabDoll.action.book_action import HandBookAction
from grabDoll.models.config_model import ConfigModel
import random
import time
__author__ = 'du_du'


def get_inventory_info(uid):
    item_action = ItemAction(uid)
    hero_action = HeroAction(uid)
    gacha_model = GachaModel(uid)
    book_action = HandBookAction(uid)

    return {
        'items': item_action.get_all(),
        'gacha': gacha_model.get_model_info(),
        'dolls': hero_action.get_model_info(),
        'book': book_action.get_model_info(),
    }


def get_config_info():
    config_group = ('egg', 'item', 'gacha', 'doll', 'machine', 'book', 'shop')
    config_data = dict()
    for config_name in config_group:
        config_data[config_name] = ConfigModel(config_name).get_model_info()
    return config_data


def add_item(uid, item_id):
    item_model = ItemAction(uid)
    res = item_model.add_model(item_id, 1)
    return res


def use_item(uid, item_id):
    if type(item_id) == 'unicode':
        config_id = item_id.encode("utf-8")
    else:
        config_id = item_id
    config_id = int(config_id)
    print type(config_id)
    item_type = config_id/10000
    print('config_id', item_id, 'item_type', item_type)
    if item_type != 2:
        return False
    # 先判定抓到的娃娃蛋存不存在
    del_res = reduce_item(uid, item_id)
    # 存在的话删除掉
    if del_res:
        # 奖励
        awards = get_award(item_id)
        item_model = ItemAction(uid)
        doll_model = HeroAction(uid)
        gacha_model = GachaModel(uid)
        book_model = HandBookAction(uid)
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
            elif int(a_id)/10000 == 2:
                if item_model.add_model(a_id, ct):
                    res[a_id] = ct
            elif int(a_id)/10000 == 3:
                gacha_model.add_model(a_id, ct)
            elif int(a_id)/10000 == 4:
                res['doll'] = doll_model.add_model(a_id)
            elif int(a_id)/10000 == 5:
                book_model.add_model(a_id, ct)
            else:
                pass
            # 如果是娃娃
            # 如果是Gacha蛋
        return res
    print("item  is not exits")
    return False


def reduce_item(uid, item_id):
    item_model = ItemAction(uid)
    return item_model.remove_model(item_id, 1)


def reduce_egg(uid, item_id):
    mach_model = MachineModel(uid)
    return mach_model.delete_egg(item_id)


def reduce_gacha(uid, item_id):
    gach_model = GachaModel(uid)
    return gach_model.remove_model(item_id)


# 查看奖励
def get_award(item_id):

    config_model = ConfigModel('item')
    config_info = config_model.get_config_by_id(item_id)
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
