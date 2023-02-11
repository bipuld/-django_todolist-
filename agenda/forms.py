from django import forms
from agenda.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['Task_name', 'status','effort'] 
        
        
    