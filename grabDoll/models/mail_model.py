# -*- coding: utf-8 -*-
from lib.redis_model import HashModel
from rest_framework import serializers
from django.db import models
from grabDoll.common.serializerutils import UnixEpochDateField
__author__ = 'du_du'


class MailModel(HashModel):
    pass


class MailTable(models.Model):
    u_id = models.CharField(max_length=32, unique=True)
    key_id = models.CharField(max_length=32, unique=True)
    fr_id = models.CharField(max_length=32,)
    info = models.CharField(max_length=512,)
    award = models.CharField(max_length=512,)
    read = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)


class MailTableSerializer(serializers.ModelSerializer):
    create_at = UnixEpochDateField(required=False, allow_null=True)
    modify_at = UnixEpochDateField(required=False, allow_null=True)

    class Meta:
        model = MailTable
        unique_together = (("u_id", "key_id"),)
        fields = '__all__'
