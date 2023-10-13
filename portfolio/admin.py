from django.contrib import admin
from .models import PortFolio



class PortFolioAdmin(admin.ModelAdmin):
    model = PortFolio
    list_display = ['id',  'project_name', 'created_at', 'created_by']
    list_display_links = ['id', 'project_name']
    readonly_fields=('created_by', 'created_at')
    search_fields = ('id', 'created_by', 'project_name')
    list_filter = ('created_by', 'created_at')

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()



admin.site.register(PortFolio, PortFolioAdmin)
