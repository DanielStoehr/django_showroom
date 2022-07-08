from django.urls import path
from rest_framework import routers

from . import views

# routerV1 = routers.DefaultRouter()
# routerV1.register("machine/{invnr}/times", views.GetTimes, basename="TimesV1")

urlpatterns = [
    path("machine/<invnr>/times", views.GetTimes2),
]
