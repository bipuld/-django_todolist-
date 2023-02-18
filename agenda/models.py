from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
# Create your models here.

class Task(models.Model):
    work_ch=(
        ('Myself', 'Myself'),
        ('Other', 'Other'),
        ('Task', 'Task'),
    )
    
    owner=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    Task_name = models.CharField(max_length=300)
    status=models.BooleanField(default=False)
    effort=models.CharField(choices=work_ch,max_length=150,default="Myself")
    Time = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.Task_name + "-" + str(self.status)


class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200,blank=False)
    email=models.EmailField(default="")
    subject=models.CharField(max_length=200,blank=False)
    # message=models.CharField(max_length=300)
    message=RichTextField()
#    phone=PhoneNumberField()
    def __str__(self):
        return self.name + "-" + (self.subject)