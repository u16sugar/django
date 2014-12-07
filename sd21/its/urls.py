# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from its import views
from django.views.generic import ListView, DetailView
from its.models import Product

urlpatterns = patterns('',
   # 問い合わせ
   url(r'^incident/$', views.incident_list, name='incident_list'),
   url(r'^incident/add$', views.incident_edit, name='incident_add'),
   url(r'^incident/mod/(?P<incident_id>\d+)/$', views.incident_edit, name='incident_mod'),                    
   url(r'^incident/del/(?P<incident_id>\d+)/$', views.incident_del, name='incident_del'),
   # 対応
   url(r'^support/(?P<incident_id>\d+)/$', views.SupportList.as_view(), name='support_list'),
   url(r'^support/add/(?P<incident_id>\d+)/$', views.support_edit, name='support_add'),
   url(r'^support/mod/(?P<incident_id>\d+)/(?P<support_id>\d+)/$', views.support_edit, name='support_mod'),
   url(r'^support/del/(?P<incident_id>\d+)/(?P<support_id>\d+)/$', views.support_del, name='support_del'),
   # 製品
   url(r'^product/$',
       ListView.as_view(
                        model=Product,
                        queryset=Product.objects.all().order_by('id'),
                        context_object_name='product_list',
                        template_name='its/product_list.html'
        )
   ),
   
   
   
                          
)
