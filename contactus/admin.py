from django.contrib import admin
from .models import ContactUs, ContactInfo



class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_display = ['id',  'email', 'created_at']
    list_display_links = ['id', 'email']
    readonly_fields=('name', 'email', 'message','created_at')
    search_fields = ('id', 'email', 'name')

    def has_add_permission(self, request, obj=None):
        return False


class ContactInfoAdmin(admin.ModelAdmin):
    model = ContactInfo
    list_display = ['id',  'email', 'call_us']
    list_display_links = ['id', 'email']
    search_fields = ('id', 'email')

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
