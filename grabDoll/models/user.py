# -*- coding: utf-8 -*-
from lib.redis_model import StringModel, HashModel
from grabDoll.models.base_model import BaseModel
from rest_framework import serializers
from django.db import models
from grabDoll.common.serializerutils import UnixEpochDateField
__author__ = 'du_du'


class UserAction(BaseModel):
    def __init__(self, u_id):
        self.u_id = u_id
        super(UserAction, self).__init__(
                    u_id, User, UserTable, UserTableSerializer, True)

    def add_gold(self, ct):
        self.incr("gold", ct)
        return True

    def add_diamond(self, ct):
        self.incr("diamond", ct)
        return True

    def add_exp(self, ct):
        self.incr("exp", ct)
        return True

    # 体力
    def add_vit(self, ct):
        self.incr("vit", ct)
        return True

    def get_model_info(self):
        data = self.get_all()
        if not data:
            # 创建新用户
            data = {
                'gold': 1000,
                'diamond': 100,
                'uid': self.u_id,
                'exp': 0,
                'lv': 1,
            }
            return self.set_values(data)
        res = {}
        key_info = ('uid', 'name', 'gold', 'diamond', 'exp', 'vit', 'lv')
        for key in key_info:
            if key in data:
                res[key] = data[key]
            else:
                res[key] = 0
        return res


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
