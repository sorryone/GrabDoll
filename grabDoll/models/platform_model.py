# -*- coding: utf-8 -*-
from lib.redis_model import HashModel
from rest_framework import serializers
from django.db import models
from grabDoll.common.serializerutils import UnixEpochDateField
__author__ = 'du_du'


class PlatformModel(HashModel):
    pass


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

