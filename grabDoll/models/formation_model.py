# -*- coding: utf-8 -*-
from lib.redis_model import HashModel
from rest_framework import serializers
from django.db import models
from grabDoll.common.serializerutils import UnixEpochDateField
__author__ = 'du_du'


class FormationModel(HashModel):
    pass


class FormationTable(models.Model):
    u_id = models.CharField(max_length=32, unique=True)
    fight_formation = models.CharField(max_length=512, null=True)
    fight_atk = models.IntegerField(default=0)
    fight_state = models.IntegerField(default=0)
    explore_formation = models.CharField(max_length=512, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)


class FormationTableSerializer(serializers.ModelSerializer):
    create_at = UnixEpochDateField(required=False, allow_null=True)
    modify_at = UnixEpochDateField(required=False, allow_null=True)

    class Meta:
        model = FormationTable
        fields = '__all__'
