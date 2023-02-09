from django.contrib import admin
from agenda.models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','Task_name','status','effort')
    list_display_links=('Task_name',)
    list_editable=('status',)
    list_filter=('id','Task_name','effort')
    search_fields=('Task_name','effort')
    
    

admin.site.register(Task,TaskAdmin)