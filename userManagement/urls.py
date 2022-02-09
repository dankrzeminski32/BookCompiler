from django.contrib import admin
from django.urls import path, include
from . import views

# This will all stem off our home path '/'
# Routes to everything that handles user creation and user customization
urlpatterns = [
    path('register/', views.registerUser, name="registerView" ),
    path('login/',views.loginUser, name="loginView"),
    path('logout/',views.logoutUser, name="logoutView"),
    path('profile/',views.userProfile, name="userProfile")
]
