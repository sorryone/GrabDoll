# -*- coding: utf-8 -*-
import datetime
import time
from django.utils.timezone import utc
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response

class UnixEpochDateField(serializers.DateTimeField):
    def to_representation(self, value):
        """ Return epoch time for a datetime object or ``None``"""
        try:
            return int(time.mktime(value.timetuple()) + (3600*8)) * 1000
        except (AttributeError, TypeError):
            return None

    def to_internal_value(self, value):
        return datetime.datetime.fromtimestamp(int(value) / 1000 - (3600*8)).replace(tzinfo = utc)