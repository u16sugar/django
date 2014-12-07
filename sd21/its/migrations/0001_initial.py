# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='受付日時')),
                ('entry_date', models.DateField(verbose_name='受付日')),
                ('entry_time', models.TimeField(verbose_name='受付時間')),
                ('entry_type', models.CharField(max_length=255, verbose_name='問い合わせ種別', choices=[('TEL', 'TEL'), ('直接', '直接（口頭）'), ('Eメール', 'Eメール'), ('監視', '監視')])),
                ('client', models.CharField(max_length=255, verbose_name='依頼者', blank=True)),
                ('contact', models.CharField(max_length=255, verbose_name='連絡者', blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='件名')),
                ('content', models.TextField(verbose_name='内容')),
            ],
            options={
                'verbose_name_plural': '問い合わせ一覧',
                'verbose_name': '問い合わせ',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inventry',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='シリアルナンバー')),
                ('user', models.CharField(max_length=255, verbose_name='使用者', blank=True)),
                ('pc_name', models.CharField(max_length=255, verbose_name='PC名', blank=True)),
                ('pc_category', models.CharField(max_length=255, verbose_name='PC種別', blank=True)),
                ('os', models.CharField(max_length=255, verbose_name='OS', blank=True)),
                ('msoffice', models.CharField(max_length=255, verbose_name='MS Offie', blank=True)),
                ('warranty_from', models.DateField(null=True, verbose_name='保証開始日', blank=True)),
                ('warranty_to', models.DateField(null=True, verbose_name='保証満了日', blank=True)),
            ],
            options={
                'verbose_name_plural': 'IT資産一覧',
                'verbose_name': 'IT資産',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='名称')),
                ('short_name', models.CharField(unique=True, max_length=255, verbose_name='略称')),
                ('segment', models.CharField(unique=True, max_length=255, verbose_name='セグメント')),
                ('shop_no', models.CharField(max_length=255, verbose_name='店舗番号', blank=True)),
                ('address', models.CharField(max_length=255, verbose_name='住所', blank=True)),
                ('tel', models.CharField(max_length=255, verbose_name='TEL', blank=True)),
                ('fax', models.CharField(max_length=255, verbose_name='FAX', blank=True)),
                ('area', models.CharField(max_length=255, verbose_name='地区', blank=True)),
            ],
            options={
                'verbose_name_plural': '場所一覧',
                'verbose_name': '場所',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='製品名')),
                ('maker', models.CharField(max_length=255, verbose_name='メーカー', blank=True)),
                ('lot', models.IntegerField(default=1, verbose_name='ロット', blank=True)),
                ('cpu', models.CharField(max_length=255, verbose_name='CPU', blank=True)),
                ('memory', models.CharField(max_length=255, verbose_name='メモリ', blank=True)),
                ('hdd', models.CharField(max_length=255, verbose_name='hdd', blank=True)),
                ('warranty', models.CharField(max_length=255, verbose_name='ハードウェア保証', blank=True)),
                ('memo', models.TextField(verbose_name='メモ', blank=True)),
            ],
            options={
                'verbose_name_plural': '製品一覧',
                'verbose_name': '製品',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='コメント')),
                ('incident', models.ForeignKey(related_name='incident_support', to='its.Incident', verbose_name='問い合わせ')),
            ],
            options={
                'verbose_name_plural': '対応一覧',
                'verbose_name': '対応',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='inventry',
            name='location',
            field=models.ForeignKey(related_name='locations', to='its.Location', verbose_name='場所'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inventry',
            name='product',
            field=models.ForeignKey(related_name='products', to='its.Product', verbose_name='製品'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='incident',
            name='inventry',
            field=models.ForeignKey(related_name='incident_Inventries', verbose_name='PC', blank=True, to='its.Inventry', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='incident',
            name='location',
            field=models.ForeignKey(related_name='incident_locations', to='its.Location', verbose_name='場所'),
            preserve_default=True,
        ),
    ]
