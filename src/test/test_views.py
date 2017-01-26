from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest.views import MealList
from django.contrib.auth.models import User
from rest.models import Schedule, ScheduleDay, Activity, Meal
import datetime

class ViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='spectacles')
        schedule = Schedule.objects.create(name='Test schedule', owner=user)
        scheduleDay = ScheduleDay.objects.create(name='Monday',schedule=schedule)
        self.user = user
        self.schedule = schedule
        self.day = scheduleDay
        print( "Created day with id: ", self.day.id )

    def tearDown(self):
        days = ScheduleDay.objects.all()
        for d in days:
            d.delete()
        schedules = Schedule.objects.all()
        for s in schedules:
            s.delete()
        users = User.objects.all()
        for u in users:
            u.delete()

    def test_something(self):
        factory = APIRequestFactory()
        view = MealList.as_view()
        postdata = {
            'day': self.day.id,
            'name': 'Dinner',
            'timeFrom': datetime.time(19),
            'timeTo': datetime.time(20)
        }

        request = factory.post('rest/meals/', postdata, format='json')
        response = view(request)

        assert response.status_code == 201  # Created
        assert "id" in response.data
        assert response.data['name'] == "Dinner"
        assert response.data['timeFrom'] == "19:00:00"
        assert response.data['timeTo'] == "20:00:00"
