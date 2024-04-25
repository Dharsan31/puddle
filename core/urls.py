from django.urls import path
from . import views
from .forms import loginform
from django.contrib.auth import views as login_view

app_name='core'
urlpatterns = [
    path('login/',login_view.LoginView.as_view(authentication_form=loginform,template_name='core/login.html'),name='login'),
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.Signup,name='signup')
]