# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grabDoll', '0007_auto_20171102_0810'),
    ]

    operations = [
        migrations.CreateModel(
            name='HatchTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u_id', models.CharField(unique=True, max_length=32)),
                ('pos', models.IntegerField(max_length=4, null=True)),
                ('key_id', models.CharField(max_length=32)),
                ('ad', models.IntegerField(default=0)),
                ('mark_at', models.IntegerField(default=0)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
