from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Service, ServiceSegment



class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ['id', 'service_name']
    list_display_links = ['id', 'service_name']
    readonly_fields=('slug', 'created_by', 'created_at')
    search_fields = ('id', 'created_by', 'service_name', 'slug')
    list_filter = ('created_by', 'created_at')

    fieldsets = [(None, {'fields':('service_name', 'image', 'details', 'segments','created_by', 'created_at', 'slug')})]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()
    
    def rel(self, obj):
        return self.links_to_objects(obj.segments.all())

    @classmethod
    def links_to_objects(cls, objects):
        rel_list = "<ol>"
        for obj in objects:
            link = "/admin/service/servicesegment/{}/change/".format(obj.id)
            rel_list += "<li><a href='%s'>%s</a></li>" % (link, obj.title)
        rel_list += "</ol>"
        return format_html(rel_list)



class ServiceSegmentAdmin(admin.ModelAdmin):
    model = Service
    list_display = ['id',  'title', 'image_tag']
    list_display_links = ['id', 'title']
    readonly_fields=('image_tag',)
    fieldsets = [(None, {'fields':('title', 'image_tag', 'image', 'figcaption', 'details')})]


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceSegment, ServiceSegmentAdmin)
