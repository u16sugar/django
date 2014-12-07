# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('its', '0003_auto_20141123_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='status',
            field=models.CharField(max_length=255, default=0, verbose_name='ステータス', choices=[('受付', '受付'), ('対応中', '対応中'), ('対応済み', '対応済み'), ('完了', '完了')]),
            preserve_default=False,
        ),
    ]
