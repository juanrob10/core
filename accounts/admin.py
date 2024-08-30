from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import  Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from unfold.admin import ModelAdmin

CustomUser = get_user_model()


admin.site.site_header = 'Proyecto'                    
admin.site.index_title = 'Areas comunes'                
admin.site.site_title = 'Panel de Admintracion' 


admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin, ModelAdmin):
	form = UserChangeForm
	add_form = UserCreationForm
	change_password_form = AdminPasswordChangeForm
	
	readonly_fields = ['date_joined','last_login']


	add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username","email","first_name","last_name","password1", "password2", 
            )}
        ),
    )
    
  
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
    
    
admin.site.register(CustomUser,UserAdmin)
admin.site.register(Group,GroupAdmin) 
    
    





