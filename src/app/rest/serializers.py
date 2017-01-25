from rest_framework.serializers import ModelSerializer
from rest.models import Meal

class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id','name','timeFrom','timeTo')