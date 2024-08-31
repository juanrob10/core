from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class LoginForm(AuthenticationForm):
    pass
    
 
class CustomUserUpdateForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(CustomUserUpdateForm,self).__init__(*args,**kwargs)
        self.fields['last_login'].widget.attrs['readonly'] = True
        self.fields['date_joined'].widget.attrs['readonly'] = True

    class Meta:
        model = CustomUser
        fields = ['username','image','first_name','last_name', 'email','last_login', 'date_joined']

