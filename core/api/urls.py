from pathlib import Path
from home.views import index, people
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('people/', people)
]