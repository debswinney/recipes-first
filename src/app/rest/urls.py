from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^meals/$', views.MealList.as_view()),
    url(r'^meals/(?P<pk>[0-9]+)/$', views.MealDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)