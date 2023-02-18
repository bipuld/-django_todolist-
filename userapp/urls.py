from django.contrib import admin
from django.urls import path,include
from  userapp import views
from django.contrib.auth import views as authorizations_views
urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',authorizations_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',authorizations_views.LogoutView.as_view(template_name='logout.html'),name='logout')
]