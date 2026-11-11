from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('home_page/', home_page, name="home_page"),
    path('add_author/', add_authors, name="add_author")
]
