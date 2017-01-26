from rest.models import Schedule, ScheduleDay, Activity, Meal
from django.contrib.auth.models import User
from django.test import TestCase
import datetime

class MealTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='spectacles')
        sched = Schedule.objects.create(name='Test schedule', owner=user)
        day1 = ScheduleDay.objects.create(name='Monday',schedule=sched)
        self.user = user
        self.sched = sched
        self.day1 = day1

    def tearDown(self):
        meals = Meal.objects.all()
        for m in meals:
            m.delete()

    def test_meals_created(self):
        # No meals to start with
        meals = Meal.objects.all()
        assert len(meals) == 0

        # Create meals
        Meal.objects.create(name="Breakfast", timeFrom=datetime.time(9), timeTo=datetime.time(10),day=self.day1)
        Meal.objects.create(name="Lunch", timeFrom=datetime.time(12), timeTo=datetime.time(13),day=self.day1)
        meals = Meal.objects.all()
        assert len(meals) == 2

        # Check meals match what we created
        meal = Meal.objects.get(pk=2)
        assert meal.name == "Lunch"
        assert meal.timeFrom == datetime.time( 12 )
        assert meal.timeTo == datetime.time( 13 )

#    def test_meals_updated(self):
#        assert False

    def test_meals_destroyed(self):
        meals = Meal.objects.all()
        assert len(meals) == 0

        # Create meal
        Meal.objects.create(name="Lunch", timeFrom=datetime.time(12), timeTo=datetime.time(13),day=self.day1)
        Meal.objects.create(name="Dinner", timeFrom=datetime.time(18), timeTo=datetime.time(19), day=self.day1)
        meals = Meal.objects.all()
        assert len( meals ) == 2

        # Delete meal
        meal = Meal.objects.get(pk=1)
        meal.delete()

        # Check it has gone
        meals = Meal.objects.all()
        assert len(meals) == 1