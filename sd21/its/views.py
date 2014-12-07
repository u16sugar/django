# -*- coding: utf-8 -*-
#from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.context_processors import request
from django.template import RequestContext
from its.forms import IncidentForm, SupportForm
from its.models import Incident, Support
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.views.generic.list import ListView
from its.forms import IncidentSearchForm

def incident_list(request):
    '''問い合わせの一覧'''
#    return HttpResponse(u'問い合わせ一覧')
    form = IncidentSearchForm()
    if request.method == 'GET':
        
        incidents = Incident.objects.all().order_by('id')
        return render_to_response('its/incident_list.html',
                              #{'incidents': incidents},
                              dict(incidents=incidents),
                              context_instance=RequestContext(request))

    elif request.method == 'POST':
        form = IncidentSearchForm(request.POST)
        incidents = Incident.objects.all()
        if form.is_valid:
            incidents = incidents.filter()

    return render_to_response('search.html',
                              {'form': form, 'incidents': incidents},
                              context_instance=RequestContext(request))


def incident_edit(request, incident_id=None):
    '''問い合わせの編集'''
    #return HttpResponse(u'問い合わせの編集')
    if incident_id:         #incident_idが指定されている（修正時）
        incident = get_object_or_404(Incident, pk=incident_id)
    else:                   # incident_idが指定されていない（追加時）
        incident = Incident()
    
    if request.method == 'POST':
        form = IncidentForm(request.POST, instance=incident)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.save()
            return redirect('its:incident_list')
    else:   # GETの時
        form =IncidentForm(instance=incident)       # インスタンスからフォームを作成
        
    return render_to_response('its/incident_edit.html',
                              dict(form=form, incident_id=incident_id),
                              context_instance=RequestContext(request))
    
#def search_incident(request, incident=None):
    
        

def incident_del(request, incident_id):
    '''問い合わせの削除'''
    #return HttpResponse(u'問い合わせの削除')
    incident = get_object_or_404(Incident, pk=incident_id)
    incident.delete()
    return redirect('its:incident_list')

class SupportList(ListView):
    '''作業の一覧'''
    context_object_name = 'supports'
    template_name = 'cms/support_list.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        incident = get_object_or_404(Incident, pk=kwargs['incident_id'])
        supports = incident.incident_support.all().order_by('id')
        self.object_list = supports

        context = self.get_context_data(object_list=self.object_list, incident=incident)
        return self.render_to_response(context)


def support_edit(request, incident_id, support_id=None):
    '''作業の編集'''
    incident = get_object_or_404(Incident, pk=incident_id)
    if support_id:
        support = get_object_or_404(Support, pk=support_id)
    else:
        support = Support()
        
    if request.method == 'POST':
        form = SupportForm(request.POST, instance=support)
        if form.is_valid():
            support = form.save(commit=False)
            support.incident = incident
            support.save()
            return redirect('its:support_list', incident_id=incident_id)
    else:
        form = SupportForm(instance=support)
    
    return render_to_response('its/support_edit.html',
                              dict(form=form, incident_id=incident_id, support_id=support_id),
                              context_instance=RequestContext(request))


def support_del(request, incident_id, support_id):
    '''作業の削除'''
    support = get_object_or_404(Support, pk=support_id)
    support.delete()
    return redirect('its:support_list', incident_id=incident_id)