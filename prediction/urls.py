# prediction/urls.py
from django.urls import path
from .views import prediction_page

urlpatterns = [
    path('predict/', prediction_page, name='predict-blood-donation'),
]
