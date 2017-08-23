# -*- coding: utf-8 -*-
__author__ = 'dudu'

from grabDoll.models.inventory_model import InventoryModel


def add_item(uid, data):
    if InventoryModel.get(uid) is None:
        return False

    u = InventoryModel(uid)
    u.set_values()
    return u


def get_item_info(uid):
    if InventoryModel.get(uid) is None:
        return False

    u = InventoryModel(uid)
    return u.get_all()

