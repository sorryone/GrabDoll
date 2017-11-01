# -*- coding: utf-8 -*-
from grabDoll.action.user_action import UserAction
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.item_action import ItemAction
__author__ = 'du_du'


# 抓完娃娃后刷新当前的图鉴
def buy(uid, shop_id):
    print('buy', uid, shop_id)
    user_action = UserAction(uid)
    item_action = ItemAction(uid)
    shop_config_model = ConfigModel('shop')
    shop_info = shop_config_model.get_config_by_id(shop_id)
    item_config_model = ConfigModel('item')
    item_info = item_config_model.get_config_by_id(shop_info.get('item_id'))
    print shop_info
    price = shop_info.get('price', 10000)
    if shop_info.get('method', 'gold') == 'gold' and price >= user_action.get_value('gold', 0):
        return False
    else:
        user_action.add_gold(-price)
    if shop_info.get('method') == 'diamond' and price >= user_action.get_value('diamond', 0):
        return False
    else:
        user_action.add_diamond(-price)
    print(item_info)
    item_action.add_model(item_info.get('config_id'), 1)
    return True


if __name__ == "__main__":
    print buy('ED57884CAA078DF9E0E08750D98CA834', '61004')
