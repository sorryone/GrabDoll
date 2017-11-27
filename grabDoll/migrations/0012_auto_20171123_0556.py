# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grabDoll', '0011_auto_20171122_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='formationtable',
            name='defend_ct',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='formationtable',
            name='fight_ct',
            field=models.IntegerField(default=0),
        ),
    ]
