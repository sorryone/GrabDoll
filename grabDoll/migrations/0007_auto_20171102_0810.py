# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grabDoll', '0006_auto_20171031_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemtable',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]
