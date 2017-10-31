# -*- coding: utf-8 -*-
from lib.redis_model import StringModel, HashModel
from rest_framework import serializers
from django.db import models
from grabDoll.common.serializerutils import UnixEpochDateField
from grabDoll.models.base_model import BaseModel
__author__ = 'du_du'


class PlatformModel(HashModel):
    pass


class PlatformAction(BaseModel):

    def __init__(self, u_id):
        self.u_id = u_id
        super(PlatformAction, self).__init__(
                    u_id, PlatformModel, PlatformTable, PlatformTableSerializer, True)

    def get_model_info(self):
        data = self.get_all()
        return data


class PlatformTable(models.Model):
    u_id = models.CharField(max_length=32, unique=True)
    country = models.CharField(max_length=32, null=True)
    city = models.CharField(max_length=32, null=True)
    province = models.CharField(max_length=32, null=True)
    gender = models.CharField(max_length=8, null=True)
    figureurl = models.CharField(max_length=32, null=True)
    login_time = models.CharField(max_length=32, null=True)
    nickname = models.CharField(max_length=32, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)


class PlatformTableSerializer(serializers.ModelSerializer):
    create_at = UnixEpochDateField(required=False, allow_null=True)
    modify_at = UnixEpochDateField(required=False, allow_null=True)

    class Meta:
        model = PlatformTable
        fields = '__all__'

