from django.urls import path, include
from . import views

# This has to do with our users personal dashboards and eventually the community dashboard
urlpatterns = [
    path('',views.userView, name="dashboardView")

]
