from django.contrib import admin
from django.urls import path, include
from . import views

# This will all stem off our home path '/'
urlpatterns = [
    path('', views.Register, name="registerView" )
]
