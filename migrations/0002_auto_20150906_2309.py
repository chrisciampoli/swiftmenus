# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swiftmenu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingrediant',
            old_name='ingrediant',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item',
            new_name='menu',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='menu',
            new_name='company',
        ),
    ]
