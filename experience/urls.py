from django.urls import path
from .views import ExperienceList

urlpatterns = [
    path('', ExperienceList.as_view(), name='experience_list'),
]
