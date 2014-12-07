from django import forms
from django.views.generic.list import ListView

class Postlist(ListView):
    model = post
    paginate_by = 2
    
    def get_queryset(self):
        query_string = ''
        if ('search' in self.request.GET) and self.request.GET['search'].strip():
            query_string = self.request.GET['search']
            entry_query = get_query(query_string, ['title', 'body',])
            query_set = post.objects.filter(entry_query).order_by('-created')
            self.request.session['searchset'] = queryset
            
        else:
            if self.request.session.get('searchset') and ('page' in self.request.GET):
                queryset = self.request.session['searchset']
            else:
                queryset = post.objects.all().order_by('-created')
                if self.request.session.get('searchset'):
                    del self.request.session['searchset']
        
        
        return queryset