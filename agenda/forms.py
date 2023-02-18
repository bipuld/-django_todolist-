from django import forms
from agenda.models import Task,Contact

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['Task_name', 'status','effort'] 
        widget={
            'status': forms.CheckboxInput()
        }
        
class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields=['name','email','subject','message']
        
        