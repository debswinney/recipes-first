from django.test import TestCase, Client
from rest_framework.test import APIClient
from rest.models import Schedule, ScheduleDay, Activity, Meal
from django.contrib.auth.models import User
import datetime

class MealApiTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='spectacles')
        self.schedule = Schedule.objects.create(name='Test Schedule', owner=self.user)
        self.scheduleday = ScheduleDay.objects.create(schedule=self.schedule, name='Someday')
        self.meal1 = Meal.objects.create( day = self.scheduleday, name="Breakfast", timeFrom=datetime.time(9), timeTo=datetime.time(10) )
        self.meal2 = Meal.objects.create( day = self.scheduleday, name="Lunch", timeFrom=datetime.time(12), timeTo=datetime.time(13))

    def tearDown(self):
        self.meal2.delete()
        self.meal1.delete()
        self.scheduleday.delete()
        self.schedule.delete()
        self.user.delete()

    def test_list_as_json(self):
        # Check request for list as json
        c = APIClient()
        resp = c.get('/rest/meals.json')
        assert resp.status_code == 200
        assert len(resp.data) == 2
        meal1 = resp.data[0]
        assert "id" in meal1
        assert meal1['id'] == 1
        assert meal1['name'] == "Breakfast"
        assert meal1['timeFrom'] == "09:00:00"
        assert meal1['timeTo'] == "10:00:00"
        meal2 = resp.data[1]
        assert meal2['id'] == 2
        assert meal2['name'] == "Lunch"
        assert meal2['timeFrom'] == "12:00:00"
        assert meal2['timeTo'] == "13:00:00"

    def test_list_as_default(self):
        c = APIClient()
        resp2 = c.get('/rest/meals/')
        assert resp2.status_code == 200
        assert len(resp2.data) == 2
        meal1 = resp2.data[0]
        assert meal1['id'] == 1
        assert meal1['name'] == "Breakfast"
        assert meal1['timeFrom'] == "09:00:00"
        assert meal1['timeTo'] == "10:00:00"
        meal2 = resp2.data[1]
        assert meal2['id'] == 2
        assert meal2['name'] == "Lunch"
        assert meal2['timeFrom'] == "12:00:00"
        assert meal2['timeTo'] == "13:00:00"

    def test_detail_as_json(self):
        c = Client()
        resp = c.get('/rest/meals/1.json')
        assert resp.status_code == 200
        assert resp.data['id'] == 1
        assert resp.data['name'] == "Breakfast"
        assert resp.data['timeFrom'] == "09:00:00"
        assert resp.data['timeTo'] == "10:00:00"

