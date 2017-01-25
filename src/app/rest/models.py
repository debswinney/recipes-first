from django.db import models

# Create your models here.
class Meal(models.Model):
    name=models.CharField(max_length=100, blank=False)
    timeFrom=models.TimeField()
    timeTo=models.TimeField()
    created = models.DateTimeField(auto_now_add=True)
    day = models.ForeignKey('rest.ScheduleDay', related_name='meals', on_delete=models.CASCADE)

class Activity(models.Model):
    name=models.CharField(max_length=100, blank=False)
    busyTimeFrom=models.TimeField()
    activityTimeFrom=models.TimeField()
    activityTimeTo=models.TimeField()
    busyTimeTo=models.TimeField()
    created = models.DateTimeField(auto_now_add=True)
    day = models.ForeignKey('rest.ScheduleDay', related_name='activities', on_delete=models.CASCADE)

class Schedule(models.Model):
    name=models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey('auth.User', related_name='schedules', on_delete=models.CASCADE)

class ScheduleDay(models.Model):
    name = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    schedule = models.ForeignKey('rest.Schedule', related_name='days', on_delete=models.CASCADE)
