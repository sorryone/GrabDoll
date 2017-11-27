# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grabDoll', '0013_auto_20171123_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='formationtable',
            name='catch_update_at',
            field=models.IntegerField(default=0),
        ),
    ]
