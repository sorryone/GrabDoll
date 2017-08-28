# -*- coding: utf-8 -*-
from lib.redis_model import StringModel, HashModel
__author__ = 'du_du'


class ConfigModel(HashModel):

    def get_model_info(self):
        data = dict()
        data['egg'] = {}
        data['egg'][10001] = {'item_id': 10001, 'name': "蓝鸡蛋", 'rad': 1.5, 'icon': "egg_blue"}
        data['egg'][10002] = {'item_id': 10002, 'name': "绿鸡蛋", 'rad': 1, 'icon': "egg_yellow"}
        data['egg'][10003] = {'item_id': 10003, 'name': "粉鸡蛋", 'rad': 0.7, 'icon': "egg_pink"}
        data['egg'][10004] = {'item_id': 10004, 'name': "金币", 'rad': 0.5, 'icon': "egg_coin"}

        data['factory'] = {}
        data['factory'][50001] = {'machine_id': 50001, 'lv': 1, 'icon': "img_factory_0", 'itemGroup': [20001, 20002, 20003, 20004]}
        data['factory'][50002] = {'machine_id': 50002, 'lv': 2, 'icon': "img_factory_1", 'itemGroup': [20001, 20002, 20003, 20004]}
        data['factory'][50003] = {'machine_id': 50003, 'lv': 3, 'icon': "img_factory_3", 'itemGroup': [20001, 20002, 20003, 20004]}
        data['factory'][50004] = {'machine_id': 50004, 'lv': 4, 'icon': "img_factory_3", 'itemGroup': [20001, 20002, 20003, 20004]}
        data['factory'][50005] = {'machine_id': 50005, 'lv': 5, 'icon': "img_factory_3", 'itemGroup': [20001, 20002, 20003, 20004]}
        data['factory'][50006] = {'machine_id': 50006, 'lv': 6, 'icon': "img_factory_3", 'itemGroup': [20001, 20002, 20003, 20004]}

        data['item'] = {}
        data['item'][20001] = {'item_id': 20001, 'name': "鸡蛋", 'icon': "img_factory_0"}
        data['item'][20002] = {'item_id': 20002, 'name': "鸡蛋", 'icon': "img_factory_1"}
        data['item'][20003] = {'item_id': 20003, 'name': "鸡蛋", 'icon': "img_factory_2"}
        data['item'][20004] = {'item_id': 20004, 'name': "鸡蛋", 'icon': "img_factory_0"}
        data['item'][20005] = {'item_id': 20005, 'name': "鸡蛋", 'icon': "img_factory_0"}
        data['item'][20006] = {'item_id': 20006, 'name': "鸡蛋", 'icon': "img_factory_0"}
        data['item'][20007] = {'item_id': 20007, 'name': "鸡蛋", 'icon': "img_factory_0"}
        data['item'][20008] = {'item_id': 20008, 'name': "鸡蛋", 'icon': "img_factory_0"}
        data['item'][20009] = {'item_id': 20009, 'name': "鸡蛋", 'icon': "img_factory_0"}
        data['item'][20010] = {'item_id': 20010, 'name': "鸡蛋", 'icon': "img_factory_0"}
        data['item'][20011] = {'item_id': 20011, 'name': "鸡蛋", 'icon': "img_factory_0"}
        data['item'][20012] = {'item_id': 20012, 'name': "鸡蛋", 'icon': "img_factory_0"}
        return data

    def get_config_by_id(self, config_id):
        type_value = int(int(config_id)/10000)
        # 先判定抓到的娃娃蛋存不存在
        types = ("null", "egg", "item", "gacha", "doll", "book")
        if len(types) >= type_value:
            config_data_list = self.get_model_info()
            configs = config_data_list.get(types[type_value])
            return configs.get(config_id, default=False)
        return False


