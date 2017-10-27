# -*- coding: utf-8 -*-
from lib.redis_model import StringModel, HashModel
from rest_framework import serializers
from django.db import models
from grabDoll.common.serializerutils import UnixEpochDateField
__author__ = 'du_du'


class ItemModel(HashModel):
    def get_model_info(self):
        return self.get_all()

    # 增加物品
    def add_model(self, item_id, num=1):
        res = self.incr(item_id, num)
        if res is not False:
            return True
        return False

    # 移除物品
    def remove_model(self, item_id, num=1):
        cur_ct = self.get_value(item_id)
        if cur_ct < num:
            return False
        res = self.incr(item_id, -num)
        if res == 0 or res is not False:
            return True
        return False


class ItemTable(models.Model):
    u_id = models.CharField(max_length=32, unique=True)
    key_id = models.CharField(max_length=32, unique=True)
    value = models.CharField(max_length=2048, null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)


class ItemTableSerializer(serializers.ModelSerializer):
    create_at = UnixEpochDateField(required=False, allow_null=True)
    modify_at = UnixEpochDateField(required=False, allow_null=True)

    class Meta:
        model = ItemTable
        fields = '__all__'
