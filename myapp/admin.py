from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseuserAdmin
from .models import User



class BaseUser(BaseuserAdmin):
    list_display = ('email','first_name','last_name','is_admin','is_staff','otp','profile_picture',)
    list_filter = ('is_admin','is_staff',)
    
    ordering = ('is_admin',)
    
    fieldsets = (
        (None, {
            "fields": (
                'email',
            ),
        }),
        ('Personal Info',{'fields':('first_name','last_name','mobile','password',)})
    )
    
    
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'mobile','profile_picture'),
        }),
    )

    filter_horizontal = ()
    list_per_page = 20  
    
admin.site.register(User,BaseUser)

