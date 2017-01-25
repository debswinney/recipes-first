from rest.models import Meal
from django.test import TestCase
import datetime

class MealTestCase(TestCase):
    def setUp(self):
        Meal.objects.create(name="Breakfast", timeFrom=datetime.time(9), timeTo=datetime.time(10))
        Meal.objects.create(name="Lunch", timeFrom=datetime.time(12), timeTo=datetime.time(13))

    def test_meals_created(self):
        meals = Meal.objects.all()
        assert len(meals) == 2

        meal = Meal.objects.get(pk=2)
        assert meal.name == "Lunch"
        assert meal.timeFrom == datetime.time( 12 )
        assert meal.timeTo == datetime.time( 13 )

#    def test_meals_updated(self):
#        assert False

    def test_meals_destroyed(self):
        meal = Meal.objects.get(pk=1)
        meal.delete()

        meals = Meal.objects.all()
        assert len(meals) == 1