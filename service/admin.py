from django.contrib import admin
from .models import Service



class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ['id',  'service_name', 'created_at', 'created_by']
    list_display_links = ['id', 'service_name']
    readonly_fields=('slug', 'created_by', 'created_at')
    search_fields = ('id', 'created_by', 'service_name', 'slug')
    list_filter = ('created_by', 'created_at')

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()



admin.site.register(Service, ServiceAdmin)
