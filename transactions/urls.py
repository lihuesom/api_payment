from django.urls import path,include
from . import views
from django.conf import settings
from rest_framework import routers

app_name = 'transactions'
urlpatterns = [
    path('process', views.paymentProcess),

]