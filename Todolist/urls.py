from django.contrib import admin
from django.urls import path,include
from agenda import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),  
    path('home',views.home,name='home'),
    path('task/',include('agenda.urls')),
    
]
