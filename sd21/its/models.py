# -*- coding: utf-8 -*-
from django.db import models
#from django.db.models.fields import BLANK_CHOICE_DASH
from django.utils import timezone
from django.forms import ModelForm

class Product(models.Model):
    '''製品'''
    #inventry = models.ForeignKey(Inventry, verbose_name=u'資産', related_name='inventries')
    name = models.CharField(u'製品名', max_length=255)
    maker = models.CharField(u'メーカー', max_length=255, blank=True)
    lot = models.IntegerField(u'ロット' , blank=True, default=1)
    cpu = models.CharField('CPU', max_length=255, blank=True)
    memory = models.CharField('メモリ', max_length=255, blank=True)
    hdd = models.CharField('hdd', max_length=255, blank=True)
    warranty = models.CharField(u'ハードウェア保証', max_length=255, blank=True)
    memo = models.TextField(u'メモ', blank=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = u'製品'            #adminサイトの表示変更
        verbose_name_plural = '製品一覧'    #adminサイトの表示変更
        

class Location(models.Model):
    '''場所'''
    name = models.CharField(u'名称', max_length=255, unique=True)
    short_name = models.CharField(u'略称', max_length=255, unique=True)
    segment = models.CharField(u'セグメント', max_length=255, unique=True)
    shop_no = models.CharField(u'店舗番号', max_length=255, blank=True)
    address = models.CharField(u'住所', max_length=255, blank=True)
    tel = models.CharField(u'TEL', max_length=255, blank=True)
    fax = models.CharField(u'FAX', max_length=255, blank=True)
    area = models.CharField(u'地区', max_length=255, blank=True)
    
    def __str__(self):
        return self.short_name
    
    class Meta:
        verbose_name = u'場所'
        verbose_name_plural = u'場所一覧'


    
class Inventry(models.Model):
    '''資産'''
    product = models.ForeignKey(Product, verbose_name=u'製品', related_name='products')
    location = models.ForeignKey(Location, verbose_name='場所', related_name='locations')
    name = models.CharField(u'シリアルナンバー', unique=True, max_length=255)
    user = models.CharField(u'使用者', max_length=255, blank=True)
    #location = models.CharField(u'場所', max_length=255, blank=True)
    pc_name = models.CharField(u'PC名', max_length=255, blank=True)
    pc_category = models.CharField(u'PC種別', max_length=255, blank=True)
    os = models.CharField(u'OS', max_length=255, blank=True)
    msoffice = models.CharField(u'MS Offie', max_length=255, blank=True)
    warranty_from = models.DateField(u'保証開始日', blank=True, null=True)
    warranty_to = models.DateField(u'保証満了日', blank=True, null=True)
    
    def __str__(self):
        return self.pc_name
    
    class Meta:
        verbose_name = u'IT資産'          #adminサイトの表示変更
        verbose_name_plural = u'IT資産一覧'     #adminサイトの表示変更

class Incident(models.Model):
    '''コール受付'''
    ENTRY_TYPE = (
        (u'TEL', u'TEL'),
        (u'直接', u'直接（口頭）'),
        (u'Eメール', u'Eメール'),
        (u'監視', u'監視'),
    )
        

    STATUS_TYPE = (
        (u'受付', u'受付'),
        (u'対応中', u'対応中'),
        (u'対応済み', u'対応済み'),
        (u'完了', u'完了'),
    )
    
    
    
    datetime = models.DateTimeField(u'受付日時' )
    #entry_date = models.DateField(u'受付日')
    #entry_time = models.TimeField(u'受付時間')
    entry_type = models.CharField(u'問い合わせ種別', max_length=255, choices=ENTRY_TYPE) 
    location = models.ForeignKey(Location, verbose_name='場所', related_name='incident_locations')
    inventry = models.ForeignKey(Inventry, blank=True, null=True, verbose_name='PC', related_name='incident_Inventries')
    client = models.CharField(u'依頼者', max_length=255, blank=True)
    contact = models.CharField(u'連絡者', max_length=255, blank=True)
    title = models.CharField(u'件名',max_length=255,)
    content = models.TextField(u'内容')
    status = models.CharField(u'ステータス', max_length=255, choices=STATUS_TYPE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'問い合わせ'          #adminサイトの表示変更
        verbose_name_plural = u'問い合わせ一覧'     #adminサイトの表示変更


class Support(models.Model):
    incident = models.ForeignKey(Incident, verbose_name='問い合わせ', related_name='incident_support')
    datetime_from = models.DateTimeField(u'対応開始日時' )
    datetime_to = models.DateTimeField(u'対応終了日時' )
    comment = models.TextField(u'対応内容')

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = u'対応'          #adminサイトの表示変更
        verbose_name_plural = u'対応一覧'     #adminサイトの表示変更
