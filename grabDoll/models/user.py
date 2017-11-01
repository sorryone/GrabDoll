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
    # password = models.CharField(max_length=128, null=True)
    # username = models.CharField(max_length=32, null=True)
    # nickname = models.CharField(max_length=32, null=True)
    # first_name = models.CharField(max_length=32, null=True)
    # last_name = models.CharField(max_length=32, null=True)
    # email = models.CharField(max_length=254, null=True)
    # checkmail = models.NullBooleanField(null=True)
    # mobile = models.CharField(max_length=16, null=True)
    # avatar_file = models.CharField(max_length=1024, null=True)
    # sex = models.IntegerField(null=True)
    # birthday = models.IntegerField(null=True)
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
