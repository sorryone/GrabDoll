# -*- coding: utf-8 -*-
from grabDoll.models.user import User as UserModel
from grabDoll.models.config_model import ConfigModel
from grabDoll.models.item_model import ItemModel

__author__ = 'du_du'


# 抓完娃娃后刷新当前的图鉴
def buy(uid, shop_id):
    print('buy', uid, shop_id)
    user_model = UserModel(uid)
    item_model = ItemModel(uid)
    shop_config_model = ConfigModel('shop')
    shop_info = shop_config_model.get_config_by_id(shop_id)
    item_config_model = ConfigModel('item')
    item_info = item_config_model.get_config_by_id(shop_info.get('item_id'))
    print shop_info
    price = shop_info.get('price', 10000)
    if shop_info.get('method', 'gold') == 'gold' and price >= user_model.get_value('gold', 0):
        return False
    else:
        user_model.add_gold(-price)
    if shop_info.get('method') == 'diamond' and price >= user_model.get_value('diamond', 0):
        return False
    else:
        user_model.add_diamond(-price)
    print(item_info)
    item_model.add_model(item_info.get('config_id'), 1)
    return True


if __name__ == "__main__":
    print buy('ED57884CAA078DF9E0E08750D98CA834', '61004')
