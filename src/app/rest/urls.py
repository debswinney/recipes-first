from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^meals/$', views.MealList.as_view()),
    url(r'^meals/(?P<pk>[0-9]+)/$', views.MealDetail.as_view()),
    url(r'^activities/$', views.ActivityList.as_view()),
    url(r'^activities/(?P<pk>[0-9]+)/$', views.ActivityDetail.as_view()),
    url(r'^scheduledays/$', views.ScheduleDayList.as_view()),
    url(r'^scheduledays/(?P<pk>[0-9]+)/$', views.ScheduleDayDetail.as_view()),
    url(r'^schedules/$', views.ScheduleList.as_view()),
    url(r'^schedules/(?P<pk>[0-9]+)/$', views.ScheduleDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)