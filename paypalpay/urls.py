from .views import initiate_payment
from django.urls import path

urlpatterns = [
    path('paypal/', initiate_payment, name='paypal'),
]