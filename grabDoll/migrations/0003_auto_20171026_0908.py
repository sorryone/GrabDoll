# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grabDoll', '0002_auto_20171026_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertable',
            name='curMachineId',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='diamond',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='exp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='gold',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='lv',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='machineLv',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='maxUnLockLv',
            field=models.IntegerField(default=0),
        ),
    ]
