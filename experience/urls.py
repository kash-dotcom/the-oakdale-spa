from django.urls import path
from .views import ExperienceList

# Experience view URLs

urlpatterns = [
    path('', ExperienceList.as_view(), name='experience_list'),
]
