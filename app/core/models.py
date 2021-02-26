from django.core.exceptions import ValidationError
from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.conf import settings
from django.core.exceptions import ValidationError
from .errors import Error as AccountError
from django.db import transaction



class BankAccount(models.Model):
    customer_name = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )
    
    def __str__(self):
        return self.customer_name


class Card(models.Model):
    bank_account = models.ForeignKey(BankAccount, 
                                     on_delete=models.CASCADE)
    card_number = models.CharField(max_length=20)
    balance = models.PositiveIntegerField(verbose_name='Current balance')
    
    @classmethod
    def create(cls, bank_account, card_number, balance=10000):
        with transaction.atomic():
            card = cls.objects.create(
                bank_account = bank_account,
                card_number = card_number,
                balance = balance
            )     
        return card
    
    @classmethod
    def withdraw(cls,amount, merchant_name, merchant_id):
        assert amount > 0
        # with transaction.atomic():
        card_account = cls.objects.select_for_update().get(bank_account,card_number)

        if card_account.balance - amount < 0:
            raise errors.InsufficientFunds(amount, account.balance)
        new_balance = card_account.balance - amount
        
        card_account.save(bank_account=bank_account,card_number=card_number,balance=new_balance)
        transaction = Transaction.create(
            card = card_account,
            amount = amount,
            merchant_name = merchant_name,
            merchant_id = merchant_id
        )
        return card_account, transaction
           
    def __str__(self):
        return self.card_number
            
    
class Transaction(models.Model):
    card = models.ForeignKey(Card, 
                             on_delete=models.CASCADE)
    merchant_name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    merchant_id = models.IntegerField()
    
    def __str__(self):
        return f"{self.amount}"
    