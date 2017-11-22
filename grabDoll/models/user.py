# -*- coding: utf-8 -*-
from lib.redis_model import HashModel
from rest_framework import serializers
from django.db import models
from grabDoll.common.serializerutils import UnixEpochDateField
__author__ = 'du_du'


class User(HashModel):
    pass


class UserTable(models.Model):
    u_id = models.CharField(max_length=32, unique=True)
    gold = models.IntegerField(default=0)
    diamond = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    vit = models.IntegerField(default=0)
    lv = models.IntegerField(default=0)
    machineLv = models.IntegerField(default=0)
    curMachineId = models.IntegerField(default=0)
    maxUnLockLv = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    login_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)


class UserTableSerializer(serializers.ModelSerializer):
    login_at = UnixEpochDateField(required=False, allow_null=True)
    create_at = UnixEpochDateField(required=False, allow_null=True)
    modify_at = UnixEpochDateField(required=False, allow_null=True)

    class Meta:
        model = UserTable
        fields = '__all__'
