from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Schedule(models.Model):
    name=models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey('auth.User', related_name='schedules', on_delete=models.CASCADE)

class ScheduleDay(models.Model):
    schedule = models.ForeignKey(Schedule, related_name='days', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)

class Activity(models.Model):
    day = models.ForeignKey(ScheduleDay, related_name='activities', on_delete=models.CASCADE)
    name=models.CharField(max_length=100, blank=False)
    busyTimeFrom=models.TimeField()
    activityTimeFrom=models.TimeField()
    activityTimeTo=models.TimeField()
    busyTimeTo=models.TimeField()
    created = models.DateTimeField(auto_now_add=True)

class Meal(models.Model):
    day = models.ForeignKey(ScheduleDay, related_name='meals', on_delete=models.CASCADE)
    name=models.CharField(max_length=100, blank=False)
    timeFrom=models.TimeField()
    timeTo=models.TimeField()
    created = models.DateTimeField(auto_now_add=True)

