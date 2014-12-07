from django.contrib import admin
from its.models import Product, Inventry, Location, Incident, Support
from django.contrib.admin.templatetags.admin_list import date_hierarchy

#admin.site.register(Product)
#admin.site.register(Inventry)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'maker',  'lot', 'cpu', 'memory', 'hdd', 'warranty')
    list_display_links = ('name',)
    search_fields = ('name', 'maker')
    
admin.site.register(Product, ProductAdmin)

class InventryAdmin(admin.ModelAdmin):
    list_display = ('id', 'pc_name', 'name', 'product', 'location', 'user','pc_category', 'os', 'msoffice' ,'warranty_from', 'warranty_to')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'pc_name', 'location__short_name', 'user', 'product__name')
    ordering = ('pc_name',)
    
admin.site.register(Inventry, InventryAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'shop_no', 'segment', 'address', 'tel', 'fax', 'area',)
    search_fields = ('name', 'short_name', 'shop_no', 'segment', 'address', 'tel', 'fax', 'area',)
    
admin.site.register(Location, LocationAdmin)

class SupportInline(admin.TabularInline):
    model = Support
    extra = 1



class IncidentAdmin(admin.ModelAdmin):
    list_display = ('status', 'datetime', 'location', 'client', 'contact', 'title', 'content',)
    date_hierarchy = 'datetime'
    list_filter = ['datetime', 'location', 'client', 'contact', 'title',]
    search_fields = ['title']
    
    inlines = [SupportInline]
    
admin.site.register(Incident, IncidentAdmin)






class SupportAdmin(admin.ModelAdmin):
    list_display = ('incident', 'datetime_from', 'datetime_to', 'comment',)  

admin.site.register(Support, SupportAdmin)