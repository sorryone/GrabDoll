# -*- coding: utf-8 -*-
from lib.redis_model import StringModel, HashModel
from rest_framework import serializers
from django.db import models
from grabDoll.common.serializerutils import UnixEpochDateField
__author__ = 'du_du'


class FriendModel(HashModel):
    pass


class FriendTable(models.Model):
    u_id = models.CharField(max_length=32)
    key_id = models.CharField(max_length=32)
    value = models.CharField(max_length=2048, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)


class FriendTableSerializer(serializers.ModelSerializer):
    create_at = UnixEpochDateField(required=False, allow_null=True)
    modify_at = UnixEpochDateField(required=False, allow_null=True)

    class Meta:
        model = FriendTable
        unique_together = (("u_id", "key_id"),)
        fields = '__all__'

