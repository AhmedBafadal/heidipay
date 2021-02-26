from django.contrib import admin
from .models import BankAccount, Card, Transaction
# from django.utils.translation import gettext as _
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



admin.site.register(BankAccount)
admin.site.register(Card)
admin.site.register(Transaction)