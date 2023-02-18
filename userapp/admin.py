from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from userapp.forms import CustomForm
from django.contrib.auth.models import User
# Register your models here.
# admin.site.register(CustomForm)

class CustomFormAdmin(UserAdmin):
    add_form=CustomForm

admin.site.unregister(User) #this is first unregistered the custom from form the admin panel
admin.site.register(User,CustomFormAdmin) #this is first unregistered the custom from form the admin panel
