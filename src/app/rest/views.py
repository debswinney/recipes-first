from django.shortcuts import render
from rest.models import Meal
from rest.serializers import MealSerializer
from rest_framework import generics

# Create your views here.
class MealList(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class MealDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
