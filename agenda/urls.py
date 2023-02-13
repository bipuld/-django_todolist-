from django.contrib import admin
from django.urls import path,include
from  agenda import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('task',views.task,name='task'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),

]