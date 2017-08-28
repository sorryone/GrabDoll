# -*- coding: utf-8 -*-

from grabDoll.models.item_model import ItemModel
from grabDoll.models.user import User
from grabDoll.models.machine_model import MachineModel
from grabDoll.models.doll_model import DollModel
from grabDoll.models.gacha_model import GachaModel
from grabDoll.models.handbook_model import HandBookModel
from grabDoll.models.config_model import ConfigModel

__author__ = 'du_du'


def get_inventory_info(uid):
    item_model = ItemModel(uid)
    mach_model = MachineModel(uid)
    doll_model = DollModel(uid)
    gacha_model = GachaModel(uid)
    book_model = HandBookModel(uid)
    data = {
        'items': item_model.get_all(),
        'eggs': mach_model.get_model_info(),
        'gacha': gacha_model.get_model_info(),
        'dolls': doll_model.get_model_info(),
        'book': book_model.get_model_info(),
    }
    return data


def get_config_info():
    config_model = ConfigModel("config")
    return config_model.get_model_info()


def add_item(uid, item_id):
    item_model = ItemModel(uid)
    res = item_model.add_item(item_id, 1)
    return res


def use_item(uid, item_id):
    if item_id is None:
        print "item_id is None"
        return False
    config_id = int(item_id.split("_")[0])
    item_type = config_id/10000
    print 'config_id', config_id, 'item_type', item_type

    # 先判定抓到的娃娃蛋存不存在
    values = {
        1: reduce_egg,
        2: reduce_item,
        3: reduce_gacha,
    }

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
        for a_id, ct in awards.iteritems():
            # 如果是金币添加金币
            if a_id == "gold":
                user.add_gold(ct)
            # 如果是钻石添加钻石
            elif a_id == "diamond":
                user.add_diamond(ct)
            # 经验
            elif a_id == "exp":
                user.add_gold(ct)
            # 如果是道具添加道具
            elif int(a_id)/10000 == 2:
                item_model.add_model(a_id, ct)
            elif int(a_id)/10000 == 3:
                gacha_model.add_model(a_id, ct)
            elif int(a_id)/10000 == 4:
                doll_model.add_model(a_id, ct)
            elif int(a_id)/10000 == 5:
                book_model.add_model(a_id, ct)
            else:
                pass
            # 如果是娃娃
            # 如果是Gacha蛋
        return awards
    print "item  is not exits"
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
    return data


# 初始化娃娃机里的娃娃蛋
def init_eggs(uid):
    mach = MachineModel(uid)
    eggs = dict()
    eggs['10001_1'] = {'id': 10001, 'x': 2, 'y': 50, 'r': 30}
    eggs['10001_2'] = {'id': 10001, 'x': 3, 'y': 50, 'r': 30}
    eggs['10001_3'] = {'id': 10001, 'x': 4, 'y': 50, 'r': 30}
    eggs['10001_4'] = {'id': 10001, 'x': 5, 'y': 50, 'r': 30}
    eggs['10001_5'] = {'id': 10001, 'x': 6, 'y': 50, 'r': 30}

    res = mach.add_egg_list(eggs)
    '''
    eggs = {
        '10001_1': {'id': 10001, 'x': 2, 'y': 50, 'r': 30},
    }
    for egg_id, data in eggs.iteritems():
        res = mach.add_egg(egg_id, data)
    '''
    return res


def gacha_speed_up(uid, item_id):
    config_id = int(item_id.split("_")[0])
    item_type = config_id / 10000
    if item_type is not 2 or reduce_item(uid, config_id) is not True:
        return 1, "使用失败"
    config_model = ConfigModel("config")
    config_info = config_model.get_config_by_id(config_id)
    if config_info and config_info.get('type', 0) == "speed":
        print config_info.get('exp', 0)
    else:
        return 1, "无效的道具"





