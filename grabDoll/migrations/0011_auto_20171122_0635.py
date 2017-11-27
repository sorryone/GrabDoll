# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grabDoll', '0010_auto_20171120_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='formationtable',
            name='fight_atk',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='formationtable',
            name='fight_state',
            field=models.IntegerField(default=0),
        ),
    ]
