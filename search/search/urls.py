
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('search_word.urls'))
]
