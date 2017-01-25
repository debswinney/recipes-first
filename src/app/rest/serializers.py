from rest_framework.serializers import ModelSerializer, ReadOnlyField
from rest.models import Meal, Activity, Schedule, ScheduleDay
from django.contrib.auth.models import User

class MealSerializer(ModelSerializer):
    day = ReadOnlyField(source='day.name')

    class Meta:
        model = Meal
        fields = ('id','name','timeFrom','timeTo','day')

class ActivitySerializer(ModelSerializer):
    day_id = ReadOnlyField(source='day.id')
    day_name = ReadOnlyField(source='day.name')

    class Meta:
        model = Activity
        fields = ('id','name','busyTimeFrom','activityTimeFrom','activityTimeTo','busyTimeTo','day_id', 'day_name')

class ScheduleSerializer(ModelSerializer):
    owner = ReadOnlyField(source='owner.username')

    class Meta:
        model = Schedule
        fields = ('id','name','days','owner')

class ScheduleDaySerializer(ModelSerializer):
    schedule_id = ReadOnlyField(source='schedule.id')
    schedule_name = ReadOnlyField(source='schedule.name')

    class Meta:
        model = ScheduleDay
        fields = ('id','name','schedule_id','schedule_name','meals','activities')

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','schedules')