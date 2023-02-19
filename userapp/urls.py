from django.contrib import admin
from django.urls import path,include
from  userapp import views
from django.contrib.auth import views as authorizations_views
urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',authorizations_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',authorizations_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    # this is for the password reset item buitl in django
#     path('reset_password',authorizations_views.PasswordResetView.as_view(),name='reset_password'),
#     path('reset_password_sent',authorizations_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
#     path('reset/<uidb64>/<token>',authorizations_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
#     path('reset_password_complete',authorizations_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    ]