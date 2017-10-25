# -*- coding: utf-8 -*-
from lib.redis_model import StringModel, HashModel
from rest_framework import serializers
from django.db import models
from grabDoll.common.serializerutils import UnixEpochDateField
__author__ = 'maxijie'


class User(HashModel):
    def add_gold(self, ct):
        self.incr("gold", ct)
        return True

    def add_diamond(self, ct):
        self.incr("diamond", ct)
        return True

    def add_exp(self, ct):
        self.incr("exp", ct)
        return True

    def get_model_info(self):
        data = self.get_all()
        res = dict()
        key_info = ('uid', 'name', 'gold', 'diamond', 'exp', 'lv', 'machineLv', 'curMachineId', 'maxUnLockLv')
        for key in key_info:
            if type(data) == dict and key in data:
                res[key] = data[key]
            else:
                res[key] = 0
        return res


class UserTable(models.Model):
    u_id = models.CharField(max_length=32, unique=True)
    gold = models.IntegerField(max_length=16, null=True)
    diamond = models.IntegerField(max_length=16, null=True)
    exp = models.IntegerField(max_length=16, null=True)
    lv = models.IntegerField(max_length=4, null=True)
    machineLv = models.IntegerField(max_length=4, null=True)
    curMachineId = models.IntegerField(max_length=16, null=True)
    maxUnLockLv = models.IntegerField(max_length=16, null=True)
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
    """
    ALTER TABLE `UserTable`
    ADD CONSTRAINT `p_id`   UNIQUE (`u_id`)
    """


class UserTableSerializer(serializers.ModelSerializer):
    login_at = UnixEpochDateField(required=False, allow_null=True)
    create_at = UnixEpochDateField(required=False, allow_null=True)
    modify_at = UnixEpochDateField(required=False, allow_null=True)

    class Meta:
        model = UserTable
        fields = '__all__'
