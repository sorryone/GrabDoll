# -*- coding: utf-8 -*-
from lib.redis_model import StringModel, HashModel
from rest_framework import serializers
from django.db import models
from grabDoll.common.serializerutils import UnixEpochDateField
__author__ = 'du_du'


class FriendModel(HashModel):
    # 移除当前娃娃机里的娃娃蛋
    def get_model_info(self):
        data = self.get_all()
        res = dict()
        for key, value in data.items():
            res[key] = eval(value)
        return res


class FriendTable(models.Model):
    u_id = models.CharField(max_length=32, unique=True)
    friend_id = models.CharField(max_length=32, unique=True)
    value = models.CharField(max_length=2048, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)


class FriendTableSerializer(serializers.ModelSerializer):
    create_at = UnixEpochDateField(required=False, allow_null=True)
    modify_at = UnixEpochDateField(required=False, allow_null=True)

    class Meta:
        model = FriendTable
        fields = '__all__'

