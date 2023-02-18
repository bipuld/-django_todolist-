from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    work_ch=(
        ('Myself', 'Myself'),
        ('Other', 'Other'),
        ('Task', 'Task'),
    )
    # sno=models.AutoField(primary_key=True)
    # owner=models.ForeignKey(User,on_delete=models.CASCADE,default=None) #this is used to for single user account
    # ownner=models.ForeignKey(User,on_delete=models.CASCADE)
    Task_name = models.CharField(max_length=300)
    status=models.BooleanField(default=False)
    effort=models.CharField(choices=work_ch,max_length=150,default="Myself")
    Time = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.Task_name + "-" + str(self.status)
      