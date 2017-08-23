# -*- coding: utf-8 -*-
__author__ = 'dudu'

from grabDoll.models.inventory_model import InventoryModel
from grabDoll.models.user import User


def use_item(uid, item_id):
    if InventoryModel.get(uid) is None:
        return False
    inven = InventoryModel(uid)
    user = User(uid)
    # 先判定抓到的娃娃蛋存不存在
    # 存在的话删除掉
    del_res = inven.reduce_item(item_id)
    if del_res:
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
                inven.add_item(a_id, ct)
            # 如果是娃娃
            # 如果是Gacha蛋
        return awards
    return False


# 查看奖励
def get_award(item_id):
    ct = 1000
    data = []
    data['gold'] = ct
    return data


# 获取所有的物品信息
def get_item_info(uid):
    if InventoryModel.get(uid) is None:
        return False
    inven = InventoryModel(uid)
    return inven.get_all()

