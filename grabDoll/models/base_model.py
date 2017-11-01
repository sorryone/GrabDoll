# -*- coding: utf-8 -*-
# from grabDoll import models
__author__ = 'maxijie'

"""
# KV 结构表
KV_MODEL_LIST = {
    "DollModel": models.doll_model.DollTable,
    "DollModelSerializer": models.doll_model.DollTableSerializer,
    "FriendModel": models.friend_model.FriendTable,
    "HandBookModel": models.handbook_model.HandBookTable,
    "ItemModel": models.item_model.ItemTable,
}

# DB 结构表
DB_MODEL_LIST = {
    "PlatformModel": models.platform_model.PlatformTable,
    "User": models.user.UserTable,
}

SERIALIZER_LIST = {
    "DollModelSerializer": models.doll_model.DollTableSerializer,
    "FriendModelSerializer": models.friend_model.FriendTableSerializer,
    "HandBookModelSerializer": models.handbook_model.HandBookTableSerializer,
    "ItemModelSerializer": models.item_model.ItemTableSerializer,
    "PlatformModelSerializer": models.platform_model.PlatformTableSerializer,
    "UserSerializer": models.user.UserTableSerializer,
}
"""


class BaseModel(object):
    def __init__(self, u_id, hash_model, model, modelSerializer, is_dbmodel):
        self.u_id = u_id
        self.hash_model = hash_model(self.u_id)
        self.class_key = self.hash_model.__class__.__name__
        # self.modelserializer_key = self.class_key + "Serializer"
        if is_dbmodel:
            self.is_DBTable = True
            self.is_KVTable = False
        else:
            self.is_DBTable = False
            self.is_KVTable = True

        self.model = model

        """
        self.modelserializer_key = self.class_key + "Serializer"
        self.is_DBTable = False
        self.is_KVTable = False

        if self.class_key in DB_MODEL_LIST:
            self.is_DBTable = True
            self.model = DB_MODEL_LIST[self.class_key]
        elif self.class_key in KV_MODEL_LIST:
            self.is_KVTable = True
            self.model = KV_MODEL_LIST[self.class_key]
        else:
            raise NotImplementedError

        self.modelSerializer = SERIALIZER_LIST[self.modelserializer_key]
        """
        self.modelSerializer = modelSerializer

    # 查看key是否存在
    def has_key(self, key):
        if self.is_DBTable:
            return key in [f.name for f in self.model._meta.fields]

        elif self.is_KVTable:
            has_data = self.hash_model.has_key(key)
            if has_data:
                return has_data

            is_has = self.model.objects.filter(
                        u_id=self.u_id, key_id=key).exists()
            return is_has

    # 获取全部的key
    def get_keys(self):
        if self.is_DBTable:
            return [f.name for f in self.model._meta.fields]

        elif self.is_KVTable:
            keys = self.hash_model.get_keys()
            if keys:
                return keys

            model_keys = self.model.objects.filter(
                    u_id=self.u_id).values_list("key_id", flat=True)
            return model_keys

    # 获取当前key的数据
    def get_value(self, key, default=None):
        if self.is_DBTable:
            try:
                model_data = self.model.objects.get(u_id=self.u_id)
            except self.model.DoesNotExist:
                return {}

            return getattr(model_data, key)

        elif self.is_KVTable:
            redis_data = self.hash_model.get_value(key)
            if redis_data:
                return redis_data

            try:
                model_data = self.model.objects.get(u_id=self.u_id, key_id=key)
            except self.model.DoesNotExist:
                print(self.model.__class__, "Not Data Error")
                return {}

            return model_data.value

    """
    # 获取多条key_list的数据
    def get_values(self, key_list):
        if self.storage_key in DB_MODEL_LIST:
            model = DB_MODEL_LIST[self.storage_key]
            model_datas = model.objects.values(*key_list).filter(u_id=self.u_id)
            return model_datas

        if self.storage_key in KV_MODEL_LIST:
            redis_datas = KV_MODEL_LIST[self.storage_key]
            if redis_datas:
                return redis_datas

            model = DB_MODEL_LIST[self.storage_key]
            model_datas = model.objects.filter(u_id=self.u_id,
                                               key_id__in=key_list)
            modelSerializer = DB_MODEL_LIST[self.modelserializer_key]
            data = modelSerializer(model_datas, many=True).data
            return data
    """

    # 获取当前用户当前表的所有数据
    def get_all(self):
        if self.is_DBTable:
            model_datas = self.model.objects.filter(u_id=self.u_id)
            data = self.modelSerializer(model_datas, many=True).data
            return data
        elif self.is_KVTable:
            redis_data = self.hash_model.get_all()
            if redis_data:
                return redis_data

            model_datas = self.model.objects.filter(u_id=self.u_id)
            data = {}
            for i in model_datas.values("key_id", "value"):
                data[i['keys_id']] = i['value']
            return data

    def set_value(self, key, value):
        if self.is_DBTable:
            try:
                model_data, is_create = self.model.objects.get_or_create(
                                            u_id=self.u_id)
            except self.model.DoesNotExist:
                print(self.model.__class__, "insert ERROR")
                return None

            model_data.key_id = key
            model_data.value = value
            model_data.save()
            data = self.modelSerializer(model_data).data
            return data

        elif self.is_KVTable:
            is_create = self.hash_model.set_value(key, value)
            try:
                model_data = self.model.objects.get_or_create(
                                u_id=self.u_id, key_id=key)
            except self.model.DoesNotExist:
                print(self.model.__class__,  "insert ERROR")
                return None

            model_data.value = value
            model_data.save()
            data = self.modelSerializer(model_data).data
            return data

    # 当前表写入批量数据
    def set_values(self, mapping):
        if self.is_DBTable:
            try:
                model_data, is_create = self.model.objects.get_or_create(
                                            u_id=self.u_id)
            except self.model.DoesNotExist:
                print(self.model.__class__,  "insert ERROR")
                return False

            for k, v in mapping.iteritems():
                if hasattr(model_data, k):
                    setattr(model_data, k, v)

            model_data.save()
            return True

        elif self.is_KVTable:
            is_ok = self.hash_model.set_values(mapping)
            if not is_ok:
                print("redis insert ERROR data is ", mapping)
                return False
            model_data = self.model.objects.filter(u_id=self.u_id,
                                                   key_id__in=mapping.keys())
            if len(model_data) != len(mapping.keys()):
                keys_list = model_data.values_list("key_id", flat=True)
                create_list = list(set(mapping.keys()).difference(
                                            set(keys_list)))
                for k_id in create_list:
                    try:
                        temp_data = self.model.create(
                                        u_id=self.u_id, key_id=k_id)
                    except self.model.DoesNotExist:
                        print(self.model.__class__, "insert ERROR")
                        continue
                    model_data.append(temp_data)

            for index in model_data:
                for k, v in mapping.iteritems():
                    if hasattr(model_data[index], k):
                        setattr(model_data[index], k, v)

                model_data[index].save()
            return True

    def incr(self, key, amount=1):
        if self.is_DBTable:
            try:
                model_data = self.model.objects.get(u_id=self.u_id)
            except self.model.DoesNotExist:
                print(self.model.__class__, "incr ERROR")
                return None

            if hasattr(model_data, key) and type(getattr(
                                    model_data, key)) in [int, long]:
                setattr(model_data, key, getattr(model_data, key) + amount)
                model_data.save()
                return getattr(model_data, key)

        elif self.is_KVTable:
            self.hash_model.incr(key, amount)
            try:
                model_data = self.model.objects.get(u_id=self.u_id, key_id=key)
            except self.model.DoesNotExist:
                print(self.model.__class__, "incr ERROR")
                return None

            if type(model_data.value) not in [int, long]:
                return None

            model_data.value += amount
            model_data.save()
            return model_data.value

    def remove(self, key):
        if self.is_DBTable:
            return None

        elif self.is_KVTable:
            is_ok = self.hash_model.pop(key)
            if not is_ok:
                return None
            try:
                model_data = self.model.objects.get(u_id=self.u_id, key_id=key)
            except self.model.DoesNotExist:
                print(self.model.__class__, "remove ERROR")
                return None

            model_data.delete()
            return True
