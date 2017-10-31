# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grabDoll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DollTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u_id', models.CharField(unique=True, max_length=32)),
                ('doll_id', models.CharField(unique=True, max_length=32)),
                ('value', models.CharField(max_length=2048)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FriendTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u_id', models.CharField(unique=True, max_length=32)),
                ('friend_id', models.CharField(unique=True, max_length=32)),
                ('value', models.CharField(max_length=2048, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HandBookTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u_id', models.CharField(unique=True, max_length=32)),
                ('book_id', models.CharField(unique=True, max_length=32)),
                ('value', models.CharField(max_length=2048)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u_id', models.CharField(unique=True, max_length=32)),
                ('item_id', models.CharField(unique=True, max_length=32)),
                ('value', models.CharField(max_length=2048)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlatformTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u_id', models.CharField(unique=True, max_length=32)),
                ('country', models.CharField(max_length=32, null=True)),
                ('city', models.CharField(max_length=32, null=True)),
                ('province', models.CharField(max_length=32, null=True)),
                ('gender', models.CharField(max_length=8, null=True)),
                ('figureurl', models.CharField(max_length=32, null=True)),
                ('login_time', models.CharField(max_length=32, null=True)),
                ('nickname', models.CharField(max_length=32, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='usertable',
            name='avatar_file',
        ),
        migrations.RemoveField(
            model_name='usertable',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='usertable',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usertable',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='usertable',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='usertable',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='usertable',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='usertable',
            name='password',
        ),
        migrations.RemoveField(
            model_name='usertable',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='usertable',
            name='username',
        ),
        migrations.AddField(
            model_name='usertable',
            name='curMachineId',
            field=models.IntegerField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='diamond',
            field=models.IntegerField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='exp',
            field=models.IntegerField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='gold',
            field=models.IntegerField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='lv',
            field=models.IntegerField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='machineLv',
            field=models.IntegerField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='maxUnLockLv',
            field=models.IntegerField(max_length=16, null=True),
        ),
    ]
