from turtle import home
from django.urls import path
from .views import home, service, contacte

urlpatterns = [
    path('', home, name='home'),
    path('service/', service, name='service'),
    path('contacte/', contacte, name='contacte'),
]

