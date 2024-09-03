from django.shortcuts import render,redirect
from .forms import LoginForm
#from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required,permission_required
#from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import CustomUser as User
from .forms import  CustomUserUpdateForm


def home_view(request):
    return render(request,'accounts/home.html')

@login_required(login_url='/accounts/login/')
def logout_view(request):
    logout(request)
    messages.info(request,"salida exitosa!")
    return render(request, 'accounts/logout.html')


@login_required(login_url='/accounts/login/')
@permission_required('is_superuser',login_url='/accounts/user/')
def list_users(request):

    users = User.objects.all()

    context = {'users': users}
    return render(request,'accounts/list_users.html',context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('accounts:user'))
      
    if request.method == 'POST':
    
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                messages.success(request,"login successful!")
                return redirect(reverse('accounts:user'))
            
        else:
        	messages.error(request, 'Error al introducir los datos	.')        
            
    else:
        form = LoginForm()
    
    param = {
        'form': form,
    }
  
    return render(request, 'accounts/login.html', param)

@login_required(login_url='/accounts/login/')
def user_view(request):
   
    return render(request, 'accounts/user.html')



@login_required(login_url='/accounts/login/')
def update_user_view(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect(reverse('accounts:profile')) 
        else:
         messages.error(request, 'Error al intentar actualizar el formulario.')     
    else:
        form = CustomUserUpdateForm(instance=request.user)

    return render(request, 'accounts/profile.html', {'form': form})    
    
    
    
    
