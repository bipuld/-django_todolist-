from django.contrib import admin
from agenda.models import Task,Contact

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','Task_name','status','effort')
    list_display_links=('Task_name',)
    list_editable=('effort',)
    list_filter=('id','Task_name')
    search_fields=('Task_name','effort')
admin.site.register(Task,TaskAdmin)



# for contact form submission

class ContactAdmin(admin.ModelAdmin):
    list_display = ('sno','name','email','subject')
    list_display_links=('name',)
    search_fields=('name','email')
    list_filter=('sno','name','email')
    # list_editable=('')
admin.site.register(Contact,ContactAdmin)