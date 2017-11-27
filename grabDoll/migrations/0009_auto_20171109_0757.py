# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grabDoll', '0008_hatchtable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hatchtable',
            name='pos',
            field=models.IntegerField(default=0),
        ),
    ]
