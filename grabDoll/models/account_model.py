# -*- coding: utf-8 -*-
from lib.redis_model import HashModel
from rest_framework import serializers
from django.db import models
from grabDoll.common.serializerutils import UnixEpochDateField
__author__ = 'du_du'


class AccountModel(HashModel):
    pass


class AccountTable(models.Model):
    u_id = models.IntegerField(default=0, unique=True)
    open_id = models.CharField(max_length=32)
    platform = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)


class AccountTableSerializer(serializers.ModelSerializer):
    create_at = UnixEpochDateField(required=False, allow_null=True)
    modify_at = UnixEpochDateField(required=False, allow_null=True)

    class Meta:
        model = AccountTable
        unique_together = (("u_id", "open_id", "platform"),)
        fields = '__all__'
