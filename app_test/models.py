from django.db import models
from django.utils import timezone


class Tasks (models.Model):
    create_time = models.TimeField(default=timezone.now)
    finish_time = models.TimeField(default=timezone.now)

    # def save_tsk(self):


class ActiveTasks(models.Model):
    time_start = models.TimeField(default=timezone.now)
    time_stop = models.TimeField(default=timezone.now)
    curr_state = models.TextField(default='NULL')
# Create your models here.
