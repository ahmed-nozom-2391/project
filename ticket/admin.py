from django.contrib import admin
from .models import Ticket



class TicketAdmin(admin.ModelAdmin):
    model = Ticket
    list_display = ['id',  'company_name', 'created_at', 'created_by']
    list_display_links = ['id', 'company_name', 'created_by']
    readonly_fields=('created_by', 'created_at')
    search_fields = ('id', 'created_by', 'company_name', 'work_field', 'problem_type')
    list_filter = ('created_by', 'created_at', 'suitable_time')
    
    def save_form(self, request, form, change):
        obj = super().save_form(request, form, change)
        if not change:
            obj.created_by = request.user
        return obj
    
    def has_add_permission(self, request, obj=None):
        return False



admin.site.register(Ticket, TicketAdmin)
