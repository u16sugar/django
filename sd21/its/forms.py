# -*- coding: utf-8 -*-
from django.forms import ModelForm, widgets
from bootstrap3_datetime.widgets import DateTimePicker
from its.models import Incident, Support
from django.core.cache.backends.db import Options
from django import forms as forms


class SearchForm(forms.Form):
    keyword = forms.CharField(label="キーワード")

class IncidentSearchForm(forms.Form):
    keyword = forms.CharField(label=u"キーワード")




class IncidentForm(ModelForm):
    '''問い合わせのフォーム'''
    class Meta:
        model = Incident

        widgets = {
            'datetime': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}),
                   }
        #keyword = forms.CharField(u'キーワード', max_length=255)
        fields = ('datetime', 'entry_type', 'location', 'client', 'contact', 'title', 'content', 'status',)
        
class SupportForm(ModelForm):
    '''対応のフォーム'''
    class Meta:
        model = Support
        
        widgets = {
            'datetime_from': DateTimePicker(options ={"format": "YYYY-MM-DD HH:mm", "showToday": True}),
            'datetime_to': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}),
                   }
        
        fields = ('datetime_from', 'datetime_to', 'comment',)