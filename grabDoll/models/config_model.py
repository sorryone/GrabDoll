# -*- coding: utf-8 -*-
from lib.redis_model import StringModel, HashModel
__author__ = 'du_du'


class ConfigModel(HashModel):

    def get_model_info(self):
        data = dict()
        data['egg'] = {}
        data['egg'][10001] = {'item_id': 10001, 'name': "蓝鸡蛋", 'rad': 0.77, 'icon': "egg_0002", 'clip': "egg_blue"}
        data['egg'][10002] = {'item_id': 10002, 'name': "绿鸡蛋", 'rad': 0.77, 'icon': "egg_0001", 'clip': "egg_yellow"}
        data['egg'][10003] = {'item_id': 10003, 'name': "粉鸡蛋", 'rad': 0.77, 'icon': "egg_0003", 'clip': "egg_red"}
        data['egg'][10004] = {'item_id': 10004, 'name': "金币", 'rad': 0.5, 'icon': "egg_coin", 'clip': "egg_red"}
        data['factory'] = {}
        data['factory'][50001] = {'machine_id': 50001, 'lv': 1, 'icon': "island_0", 'itemGroup': [20001, 20002, 20003, 20004]}
        data['factory'][50002] = {'machine_id': 50002, 'lv': 2, 'icon': "island_0", 'itemGroup': [20001, 20002, 20003, 20004]}
        data['factory'][50003] = {'machine_id': 50003, 'lv': 3, 'icon': "island_0", 'itemGroup': [20001, 20002, 20003, 20004]}
        data['factory'][50004] = {'machine_id': 50004, 'lv': 4, 'icon': "island_0", 'itemGroup': [20001, 20002, 20003, 20004]}
        data['factory'][50005] = {'machine_id': 50005, 'lv': 5, 'icon': "island_0", 'itemGroup': [20001, 20002, 20003, 20004]}
        data['factory'][50006] = {'machine_id': 50006, 'lv': 6, 'icon': "island_0", 'itemGroup': [20001, 20002, 20003, 20004]}
        data['item'] = {}
        data['item'][20001] = {'item_id': 20001, 'c_type': 2, 'exp': 100, 'name': "加速器100", 'icon': "img_factory_0"}
        data['item'][20002] = {'item_id': 20002, 'c_type': 2, 'exp': 200, 'name': "加速器200", 'icon': "img_factory_1"}
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
        data['doll'] = {}
        data['doll'][40001] = {'c_id': 40001, 'name': "胖娃娃", 'icon': "img_factory_0", 'clip': "pet_0001"}
        data['doll'][40002] = {'c_id': 40002, 'name': "白娃娃", 'icon': "img_factory_0", 'clip': "pet_0002"}
        data['doll'][40003] = {'c_id': 40003, 'name': "白娃娃", 'icon': "img_factory_0", 'clip': "pet_0003"}
        data['doll'][40004] = {'c_id': 40004, 'name': "白娃娃", 'icon': "img_factory_0", 'clip': "pet_0004"}
        data['doll'][40005] = {'c_id': 40005, 'name': "白娃娃", 'icon': "img_factory_0", 'clip': "pet_0005"}
        data['doll'][40006] = {'c_id': 40006, 'name': "白娃娃", 'icon': "img_factory_0", 'clip': "pet_0006"}
        data['doll'][40007] = {'c_id': 40007, 'name': "白娃娃", 'icon': "img_factory_0", 'clip': "pet_0007"}
        data['doll'][40008] = {'c_id': 40008, 'name': "白娃娃", 'icon': "img_factory_0", 'clip': "pet_0008"}
        return data

    def get_config_by_id(self, config_id):
        type_value = int(int(config_id)/10000)
        # 先判定抓到的娃娃蛋存不存在
        types = ("null", "egg", "item", "gacha", "doll", "book")
        if len(types) >= type_value:
            config_data_list = self.get_model_info()
            configs = config_data_list.get(types[type_value], False)
            if configs:
                return configs.get(config_id, False)
        return False


