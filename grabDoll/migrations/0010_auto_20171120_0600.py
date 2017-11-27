# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grabDoll', '0009_auto_20171109_0757'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormationTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u_id', models.CharField(unique=True, max_length=32)),
                ('fight_formation', models.CharField(max_length=512, null=True)),
                ('explore_formation', models.CharField(max_length=512, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='hatchtable',
            name='pos',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
