from django.contrib import admin
from .models import ContactUs



class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_display = ['id',  'email', 'created_at']
    list_display_links = ['id', 'email']
    readonly_fields=('name', 'email', 'message','created_at')
    search_fields = ('id', 'email', 'name')

    def has_add_permission(self, request, obj=None):
        return False
    

admin.site.register(ContactUs, ContactUsAdmin)
