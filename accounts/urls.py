from . import views
from django.urls import path


app_name ='accounts'

urlpatterns = [
    path('',views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('user/', views.user_view, name='user'),
    path('profile/', views. update_user_view,name='profile'),
    path('users/',views.list_users,name ='users'),
    path('logout', views.logout_view, name='logout'),
]
