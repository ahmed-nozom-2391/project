from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import MyUser


admin.site.site_header = 'IPAM'




class CustomUserAdmin(UserAdmin):
    model = MyUser
    list_display = [ 'phone', 'email', 'is_staff', 'is_superuser']
    list_display_links = ['phone']
    list_editable = ('is_staff', )
    
    search_fields   = ('email', 'phone',)
    list_filter     = ('is_superuser', 'date_joined', 'is_staff')
    readonly_fields =('date_joined', 'last_login', 'username')
    
    fieldsets = (
        (None, 
            {'fields': ('first_name', 'last_name','username', 'email', 'password', 'phone', 'avatar')}
        ),
        ('Permissions',
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = ( (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'phone', 'username', 'is_superuser', 'avatar')}
        ),
                    )
    



admin.site.unregister(Group)
admin.site.register(MyUser, CustomUserAdmin)
