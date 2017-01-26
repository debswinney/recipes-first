from rest_framework.serializers import ModelSerializer, ReadOnlyField, PrimaryKeyRelatedField
from rest.models import Meal, Activity, Schedule, ScheduleDay
from django.contrib.auth.models import User

class ScheduleSerializer(ModelSerializer):
    owner = ReadOnlyField(source='owner.username')
    class Meta:
        model = Schedule
        fields = ('id','name','days','owner')

class ScheduleDaySerializer(ModelSerializer):
    class Meta:
        model = ScheduleDay
        fields = ('id','schedule','name','meals','activities')

class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id','day','name','timeFrom','timeTo')

class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id','day','name','busyTimeFrom','activityTimeFrom','activityTimeTo','busyTimeTo')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','schedules')