from django.contrib import admin
from django.urls import path,include
from  agenda import views

urlpatterns = [
    path('',views.task,name='task'),
    path('task',views.task,name='task'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('completed/<task_id>',views.as_completed,name='as_completed'),
    path('incompleted/<task_id>',views.as_incompleted,name='as_incompleted'),
    path('delete/<task_id>',views.deleted,name='delete'),
    path('edit/<task_id>',views.edit_task,name='edit'),
]