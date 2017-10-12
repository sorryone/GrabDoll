# -*- coding: utf-8 -*-

from grabDoll.models.item_model import ItemModel
from grabDoll.models.user import User
from grabDoll.models.machine_model import MachineModel
from grabDoll.models.doll_model import DollModel
from grabDoll.models.gacha_model import GachaModel
from grabDoll.models.handbook_model import HandBookModel
from grabDoll.models.config_model import ConfigModel
from grabDoll.models.note_model import NoteModel
import random
import time
__author__ = 'du_du'


def get_inventory_info(uid):
    item_model = ItemModel(uid)
    doll_model = DollModel(uid)
    gacha_model = GachaModel(uid)
    book_model = HandBookModel(uid)

    return {
        'items': item_model.get_all(),
        'gacha': gacha_model.get_model_info(),
        'dolls': doll_model.get_model_info(),
        'book': book_model.get_model_info(),
    }


def get_config_info():
    config_group = ('egg', 'item', 'gacha', 'doll', 'machine', 'book', 'shop')
    config_data = dict()
    for config_name in config_group:
        config_data[config_name] = ConfigModel(config_name).get_model_info()
    return config_data


def add_item(uid, item_id):
    item_model = ItemModel(uid)
    res = item_model.add_item(item_id, 1)
    return res


def use_item(uid, item_id):
    if item_id is None:
        print("item_id is None")
        return False
    config_id = int(item_id.split("_")[0])
    item_type = config_id/10000
    print('config_id', config_id, 'item_type', item_type)

    # 先判定抓到的娃娃蛋存不存在
    values = {
        1: reduce_egg,
        2: reduce_item,
        3: reduce_gacha,
    }
    # 如果不是应该有的类型直接返回错误
    if item_type not in values:
        return False
    del_res = values.get(item_type)(uid, item_id)
    # 存在的话删除掉
    if del_res:
        # 奖励
        awards = get_award(item_id)
        item_model = ItemModel(uid)
        doll_model = DollModel(uid)
        gacha_model = GachaModel(uid)
        book_model = HandBookModel(uid)
        user = User(uid)
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
                item_model.add_model(a_id, ct)
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
    item_model = ItemModel(uid)
    return item_model.remove_model(item_id, 1)


def reduce_egg(uid, item_id):
    mach_model = MachineModel(uid)
    return mach_model.delete_egg(item_id)


def reduce_gacha(uid, item_id):
    gach_model = GachaModel(uid)
    return gach_model.remove_model(item_id)


# 查看奖励
def get_award(item_id):
    ct = 1000
    data = dict()
    data['gold'] = ct
    doll_id = random.randint(40001, 40008)
    data[doll_id] = 1
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


use_item('ED57884CAA078DF9E0E08750D98CA834','50001_17')
