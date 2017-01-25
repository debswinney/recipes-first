from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest.views import MealList
import datetime

class ViewTest(TestCase):
    def SetUp(self):
        pass

    def test_something(self):
        factory = APIRequestFactory()
        view = MealList.as_view()

        request = factory.post('rest/meals/', {'name': 'Dinner', 'timeFrom': datetime.time(19), 'timeTo': datetime.time(20)}, format='json')
        response = view(request)

        assert response.status_code == 201  # Created
        assert "id" in response.data
        assert response.data['name'] == "Dinner"
        assert response.data['timeFrom'] == "19:00:00"
        assert response.data['timeTo'] == "20:00:00"
