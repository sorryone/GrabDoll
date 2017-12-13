# -*- coding: utf-8 -*-
from lib.redis_model import HashModel
from rest_framework import serializers
from django.db import models
from grabDoll.common.serializerutils import UnixEpochDateField
__author__ = 'du_du'


class PveModel(HashModel):
    pass


class PveTable(models.Model):
    u_id = models.CharField(max_length=32, unique=True)
    pve_id = models.IntegerField(default=0)
    loss_hp = models.IntegerField(default=0)
    fight_refresh_time = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)


class PveTableSerializer(serializers.ModelSerializer):
    create_at = UnixEpochDateField(required=False, allow_null=True)
    modify_at = UnixEpochDateField(required=False, allow_null=True)

    class Meta:
        model = PveTable
        fields = '__all__'
