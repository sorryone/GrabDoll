# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grabDoll', '0003_auto_20171026_0908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dolltable',
            old_name='doll_id',
            new_name='key_id',
        ),
        migrations.RenameField(
            model_name='friendtable',
            old_name='friend_id',
            new_name='key_id',
        ),
        migrations.RenameField(
            model_name='handbooktable',
            old_name='book_id',
            new_name='key_id',
        ),
        migrations.RenameField(
            model_name='itemtable',
            old_name='item_id',
            new_name='key_id',
        ),
    ]
