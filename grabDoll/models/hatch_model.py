# -*- coding: utf-8 -*-
from lib.redis_model import HashModel
from rest_framework import serializers
from django.db import models
from grabDoll.common.serializerutils import UnixEpochDateField
__author__ = 'du_du'


class HatchModel(HashModel):
    pass


class HatchModelTable(models.Model):
    u_id = models.CharField(max_length=32, unique=True)
    left = models.CharField(max_length=512, null=True)
    center = models.CharField(max_length=512, null=True)
    right = models.CharField(max_length=512, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)


class HatchTableSerializer(serializers.ModelSerializer):
    create_at = UnixEpochDateField(required=False, allow_null=True)
    modify_at = UnixEpochDateField(required=False, allow_null=True)

    class Meta:
        model = HatchModelTable
        fields = '__all__'
