from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import api

# router = DefaultRouter()
# router.register('accounts', api.BankAccountViewSet)
# router.register('cards', api.CardViewSet)
# router.register('transactions', api.TransactionViewSet)


app_name = 'core'

urlpatterns = [
    path('cards', api.CardView.as_view())
]
