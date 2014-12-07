# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('its', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='entry_date',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='entry_time',
        ),

    ]
