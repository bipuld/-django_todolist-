from django.contrib import admin
from django.urls import path,include
from  agenda import views

urlpatterns = [
    path('',views.task_home,name='task_home'),
    path('home',views.task_home,name='task_home'),
]
