# -*- coding: utf-8 -*-
from lib.redis_model import HashModel
from rest_framework import serializers
from django.db import models
from grabDoll.common.serializerutils import UnixEpochDateField
__author__ = 'du_du'


class HatchModel(HashModel):
    pass


class HatchTable(models.Model):
    u_id = models.CharField(max_length=32, unique=True)
    pos = models.IntegerField(max_length=4, null=True)
    key_id = models.CharField(max_length=32)
    ad = models.IntegerField(default=0)
    mark_at = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)


class HatchTableSerializer(serializers.ModelSerializer):
    create_at = UnixEpochDateField(required=False, allow_null=True)
    modify_at = UnixEpochDateField(required=False, allow_null=True)

    class Meta:
        model = HatchTable
        unique_together = (("u_id", "pos"),)
        fields = '__all__'
