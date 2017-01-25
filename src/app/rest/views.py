from rest.models import Meal, Activity, ScheduleDay, Schedule
from rest.serializers import MealSerializer, UserSerializer, ActivitySerializer, ScheduleSerializer, ScheduleDaySerializer
from rest_framework import generics
from django.contrib.auth.models import User

# Create your views here.
class MealList(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class MealDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ScheduleDayList(generics.ListCreateAPIView):
    queryset = ScheduleDay.objects.all()
    serializer_class = ScheduleDaySerializer

class ScheduleDayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScheduleDay.objects.all()
    serializer_class = ScheduleDaySerializer

class ScheduleList(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
