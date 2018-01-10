# -*- coding: utf-8 -*-
from lib.redis_model import HashModel
from rest_framework import serializers
from django.db import models
from grabDoll.common.serializerutils import UnixEpochDateField
__author__ = 'du_du'


class RecordModel(HashModel):
    pass


class RecordTable(models.Model):
    u_id = models.CharField(max_length=32, unique=True)
    day_id = models.IntegerField(default=0)
    grab_doll = models.IntegerField(default=0)
    get_hero = models.IntegerField(default=0)
    cost_gold = models.IntegerField(default=0)
    cost_diamond = models.IntegerField(default=0)
    buy_vit = models.IntegerField(default=0)
    rob = models.IntegerField(default=0)
    fight = models.IntegerField(default=0)
    fight_victory = models.IntegerField(default=0)
    fight_fail = models.IntegerField(default=0)
    defend = models.IntegerField(default=0)
    defend_victory = models.IntegerField(default=0)
    defend_fail = models.IntegerField(default=0)
    box_ct = models.IntegerField(default=0)
    day_task_group = models.CharField(max_length=512, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)


class RecordTableSerializer(serializers.ModelSerializer):
    create_at = UnixEpochDateField(required=False, allow_null=True)
    modify_at = UnixEpochDateField(required=False, allow_null=True)

    class Meta:
        model = RecordTable
        unique_together = (("u_id", "day_id"),)
        fields = '__all__'
