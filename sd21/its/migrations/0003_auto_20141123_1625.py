# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('its', '0002_auto_20141123_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='support',
            name='datetime_from',
            field=models.DateTimeField(default="2014-11-23 07:28:51" , verbose_name='対応開始日時'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='support',
            name='datetime_to',
            field=models.DateTimeField(default="2014-11-23 07:28:51", verbose_name='対応終了日時'),
            preserve_default=False,
        ),
    ]
