from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('summary', views.api_summary, name='api_summary'),
    path('group', views.api_group, name='api_group'),
]
