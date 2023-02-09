from django.db import models
from datetime import datetime
# Create your models here.

class Task(models.Model):
    work_for=(
           ('myself','myself'),   
           ('other','other'),
           ('pratice','pratice'), 
             )
    Task_name = models.CharField(max_length=300)
    status=models.BooleanField(default=False)
    effort=models.CharField(choices=work_for,default='myself',max_length=150)
    Time=models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return self.Task_name + "-" + str(self.status)