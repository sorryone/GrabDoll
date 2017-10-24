# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u_id', models.CharField(unique=True, max_length=32)),
                ('password', models.CharField(max_length=128, null=True)),
                ('username', models.CharField(max_length=32, null=True)),
                ('nickname', models.CharField(max_length=32, null=True)),
                ('first_name', models.CharField(max_length=32, null=True)),
                ('last_name', models.CharField(max_length=32, null=True)),
                ('email', models.CharField(max_length=254, null=True)),
                ('mobile', models.CharField(max_length=16, null=True)),
                ('avatar_file', models.CharField(max_length=1024, null=True)),
                ('sex', models.IntegerField(null=True)),
                ('birthday', models.IntegerField(null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('login_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
