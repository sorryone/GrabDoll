# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grabDoll', '0004_auto_20171030_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dolltable',
            name='key_id',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='dolltable',
            name='u_id',
            field=models.CharField(max_length=32),
        ),
    ]
