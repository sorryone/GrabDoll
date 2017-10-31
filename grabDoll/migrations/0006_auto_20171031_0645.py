# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grabDoll', '0005_auto_20171031_0355'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='vit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='friendtable',
            name='key_id',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='friendtable',
            name='u_id',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='handbooktable',
            name='key_id',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='handbooktable',
            name='u_id',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='itemtable',
            name='key_id',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='itemtable',
            name='u_id',
            field=models.CharField(max_length=32),
        ),
    ]
