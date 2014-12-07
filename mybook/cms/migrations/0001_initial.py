# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='書籍名', max_length=255)),
                ('publisher', models.CharField(blank=True, verbose_name='出版社', max_length=255)),
                ('page', models.IntegerField(blank=True, verbose_name='ページ数', default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('comment', models.TextField(blank=True, verbose_name='コメント')),
                ('book', models.ForeignKey(related_name='impressions', verbose_name='書籍', to='cms.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
