# -*- coding: utf-8 -*-

from grabDoll.models.item_model import ItemModel
from grabDoll.models.user import User
from grabDoll.models.machine_model import MachineModel
__author__ = 'du_du'


def get_inventory_info(uid):
    item_model = ItemModel(uid)
    mach = MachineModel(uid)
    data = {
        'items': item_model.get_all(),
        'eggs': mach.get_all(),
        'gacha': [],
        'dolls': [],
    }
    return data


def add_item(uid, item_id):
    item_model = ItemModel(uid)
    res = item_model.add_item(item_id, 1)
    return res


def use_item(uid, item_id):
    if item_id is None:
        print "item_id is None"
        return False
    config_id = item_id.split("_")[0]
    item_type = config_id/10000
    print 'config_id', config_id, 'item_type', item_type
    if ItemModel.get(uid) is None:
        print "InventoryModel is None"
        return False

    item_model = ItemModel(uid)
    user = User(uid)
    # 先判定抓到的娃娃蛋存不存在
    # 存在的话删除掉
    del_res = item_model.reduce_item(item_id)

    if del_res:
        print del_res
        # 奖励
        awards = get_award(item_id)
        for a_id, ct in awards:
            # 如果是金币添加金币
            if a_id == "gold":
                user.add_gold(ct)
            # 如果是钻石添加钻石
            if a_id == "diamond":
                user.add_(ct)
            # 经验
            if a_id == "exp":
                user.add_gold(ct)
            # 如果是道具添加道具
            if a_id/1000 == 2:
                item_model.add_item(a_id, ct)
            # 如果是娃娃
            # 如果是Gacha蛋
        return awards
    print "item  is not exits"
    return False


# 查看奖励
def get_award(item_id):
    ct = 1000
    data = []
    data['gold'] = ct
    return data


# 获取所有的物品信息
def get_item_info(uid):
    if ItemModel.get(uid) is None:
        return False
    item_model = ItemModel(uid)
    return item_model.get_all()


def get_egg_info(uid):
    if MachineModel.get(uid) is None:
        return False
    mach = MachineModel(uid)
    data = mach.get_machine_info()
    return data


def init_eggs(uid):
    if MachineModel.get(uid) is None:
        print uid, "MachineModel is None"
        return False
    mach = MachineModel(uid)
    eggs = dict()
    eggs['10001_1'] = {'id': 10001, 'x': 2, 'y': 50, 'r': 30}
    eggs['10001_2'] = {'id': 10001, 'x': 3, 'y': 50, 'r': 30}
    eggs['10001_3'] = {'id': 10001, 'x': 4, 'y': 50, 'r': 30}
    eggs['10001_4'] = {'id': 10001, 'x': 5, 'y': 50, 'r': 30}

    res = mach.add_egg_list(eggs)
    '''
    eggs = {
        '10001_1': {'id': 10001, 'x': 2, 'y': 50, 'r': 30},
    }
    for egg_id, data in eggs.iteritems():
        res = mach.add_egg(egg_id, data)
    '''

    return res



