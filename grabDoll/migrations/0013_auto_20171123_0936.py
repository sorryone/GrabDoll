# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grabDoll', '0012_auto_20171123_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='formationtable',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='formationtable',
            name='capacity_update_at',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='formationtable',
            name='income',
            field=models.IntegerField(default=0),
        ),
    ]
