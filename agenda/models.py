from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Task(models.Model):
    work_ch=(
        ('Myself', 'Myself'),
        ('Other', 'Other'),
        ('Task', 'Task'),
    )
    # sno=models.AutoField(primary_key=True)
    Task_name = models.CharField(max_length=300)
    status=models.BooleanField(default=False)
    effort=models.CharField(choices=work_ch,max_length=150,default="Myself")
    Time = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.Task_name + "-" + str(self.status)
      