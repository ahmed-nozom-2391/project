from django.contrib import admin
from .models import AccountMessage



class AccountMessageAdmin(admin.ModelAdmin):
    model = AccountMessage
    list_display = ['id',  'created_by', 'created_at']
    list_display_links = ['id', 'created_by']
    readonly_fields=('created_by','message','created_at')
    search_fields = ('id', 'created_by')

    def has_add_permission(self, request, obj=None):
        return False
    

admin.site.register(AccountMessage, AccountMessageAdmin)
