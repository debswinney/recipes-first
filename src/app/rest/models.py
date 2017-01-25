from django.db import models

# Create your models here.
class Meal(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100, blank=False)
    timeFrom=models.TimeField()
    timeTo=models.TimeField()

class Activity(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100, blank=False)
    busyTimeFrom=models.TimeField()
    activityTimeFrom=models.TimeField()
    activityTimeTo=models.TimeField()
    busyTimeTo=models.TimeField()

class Schedule(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100, blank=False)
