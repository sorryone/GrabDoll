# -*- coding: utf-8 -*-
from django.db.models.fields import IntegerField
# from grabDoll import models
from django.db.models import Avg,Max
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
            model_keys = self.model.objects.filter(
                    u_id=self.u_id).values_list(
                    "key_id", flat=True).exclude(key_id__in=keys)
            return list(set(keys + list(model_keys)))

    # 获取当前key的数据
    def get_value(self, key, manydict={}):
        if self.is_DBTable:
            if not manydict:
                model_data = self.model.objects.filter(
                        u_id=self.u_id).values(key)
                data = model_data.values_list(key, flat=True)
                if len(data) == 1:
                    data = data[0]
            else:
                try:
                    model_data = self.model.objects.get(
                                    u_id=self.u_id, **manydict)
                except self.model.DoesNotExist:
                    return None

                data = getattr(model_data, key)
            return data

        elif self.is_KVTable:
            redis_data = self.hash_model.get_value(key)
            if redis_data:
                return redis_data

            try:
                model_data = self.model.objects.get(u_id=self.u_id, key_id=key)
            except self.model.DoesNotExist:
                print(self.model.__class__, "Not Data Error")
                return None

            # 反写redis
            self.hash_model.set_value(key, model_data.value)
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

    # 获得多个人的信息
    def get_all_by_userlist(self, userList, manydict={}):
        if self.is_DBTable:
            model_data = self.model.objects.filter(u_id__in=userList, **manydict)
            data = self.modelSerializer(model_data, many=True).data
            if len(data) == 1:
                # data = data[0]
                pass
            return data
        return False

    # 获取上一个用户的ID
    def get_last_id(self):
        if self.is_DBTable:
            try:
                last_id = self.model.objects.aggregate(Max('id')).values()[0]
            except self.model.DoesNotExist:
                print(self.model.__class__, "No Data")
                return 1
            if last_id is not None:
                return last_id
        return 0

    # 获取账号
    def get_user_id_by_matching(self, manydict={}):
        if self.is_DBTable:
            model_data = self.model.objects.filter(**manydict)
            data = self.modelSerializer(model_data, many=True).data
            if len(data) > 1:
                raise ValueError
            return data
        return False

    # 获取当前用户当前表的所有数据
    def get_all(self, manydict={}):
        if self.is_DBTable:
            model_data = self.model.objects.filter(u_id=self.u_id, **manydict)
            data = self.modelSerializer(model_data, many=True).data
            if len(data) == 1:
                data = data[0]
            return data

        elif self.is_KVTable:
            redis_data = self.hash_model.get_all()
            model_datas = self.model.objects.filter(
                    u_id=self.u_id).exclude(key_id__in=redis_data.keys())
            data = {}
            for i in model_datas.values("key_id", "value"):
                data[i['key_id']] = i['value']

            # 反写redis 中没有 db已有的数据
            if data:
                self.hash_model.set_values(data)
                redis_data.update(data)
            return redis_data

    def set_value(self, key, value, manydict={}):
        if self.is_DBTable:
            try:
                model_data, is_create = self.model.objects.get_or_create(
                                            u_id=self.u_id, **manydict)
            except self.model.DoesNotExist:
                print(self.model.__class__, "insert ERROR")
                return None

            setattr(model_data, key, value)
            model_data.save()
            return True

        elif self.is_KVTable:
            try:
                model_data, is_create = self.model.objects.get_or_create(
                                u_id=self.u_id, key_id=key)
            except self.model.DoesNotExist:
                print(self.model.__class__,  "insert ERROR")
                return None

            model_data.value = value
            model_data.save()
            self.hash_model.set_value(key, value)
            return True

    # 当前表写入批量数据
    def set_values(self, mapping, manydict={}):
        if self.is_DBTable:
            try:
                model_data, is_create = self.model.objects.get_or_create(
                                            u_id=self.u_id, **manydict)
            except self.model.DoesNotExist:
                print(self.model.__class__,  "insert ERROR")
                return None

            for k, v in mapping.iteritems():
                if hasattr(model_data, str(k)):
                    setattr(model_data, str(k), v)

            model_data.save()
            return True

        elif self.is_KVTable:
            model_data = self.model.objects.filter(u_id=self.u_id,
                                                   key_id__in=mapping.keys())
            if len(model_data) != len(mapping.keys()):
                keys_list = model_data.values_list("key_id", flat=True)
                create_list = list(set(mapping.keys()).difference(
                                            set(keys_list)))
                for k_id in create_list:
                    try:
                        temp_data = self.model.objects.create(
                                        u_id=self.u_id, key_id=k_id)
                    except self.model.DoesNotExist:
                        print(self.model.__class__, "insert ERROR")
                        continue
                    temp_data.value = mapping[k_id]
                    temp_data.save()

            for d in model_data:
                for k, v in mapping.iteritems():
                    if d.key_id == k:
                        d.value = str(v)
                        d.save()

            self.hash_model.set_values(mapping)
            return True

    # 当前表写入批量数据
    def update_values(self, mapping, manydict={}):
        if self.is_DBTable:
            model_data = self.model.objects.filter(u_id=self.u_id,
                                                   **manydict)
            for data in model_data:
                for k, v in mapping.iteritems():
                    if hasattr(data, str(k)):
                        setattr(data, str(k), v)
                data.save()
            datas = self.modelSerializer(model_data, many=True).data
            if len(datas) == 1:
                datas = datas[0]
            return datas
        elif self.is_KVTable:
            return False

    def incr(self, key, amount=1, manydict={}):
        if self.is_DBTable:
            value = self.model._meta.get_field(key)
            if not isinstance(value, IntegerField):
                print("This Value is not IntegerField")
                return None
            try:
                model_data, is_create = self.model.objects.get_or_create(
                            u_id=self.u_id, **manydict)
            except self.model.DoesNotExist:
                print(self.model.__class__, "incr ERROR")
                return None

            if hasattr(model_data, str(key)):
                setattr(model_data, key, getattr(model_data, key) + amount)
                model_data.save()
                return getattr(model_data, key)

        elif self.is_KVTable:
            value = self.model._meta.get_field("value")
            if not isinstance(value, IntegerField):
                print("This Value is not IntegerField")
                return None
            try:
                model_data, is_create = self.model.objects.get_or_create(
                                u_id=self.u_id, key_id=key)
            except self.model.DoesNotExist:
                print(self.model.__class__, "incr ERROR")
                return None

            model_data.value += amount
            model_data.save()
            self.hash_model.incr(key, amount)
            return model_data.value

    def remove(self, key, manydict={}):
        if self.is_DBTable:
            model_data = self.model.objects.filter(u_id=self.u_id, **manydict)
            for i in model_data:
                i.delete()

            return None

        elif self.is_KVTable:
            if manydict:
                return False
            try:
                model_data = self.model.objects.get(u_id=self.u_id, key_id=key)
            except self.model.DoesNotExist:
                print(self.model.__class__, "remove ERROR")
                return None
            model_data.delete()
            self.hash_model.pop(key)
            return True
