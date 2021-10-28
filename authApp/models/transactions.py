from django.db import models
from .account import Account

class Transactions(models.Model):
    id              = models.AutoField(primary_key=True),
    account_origin  = models.ForeignKey(Account, related_name='origin', on_delete=models.CASCADE),
    account_destiny = models.ForeignKey(Account, related_name='destiny', on_delete=models.CASCADE),
    amount          = models.IntegerField(default=0),
    register_date   = models.DateTimeField(auto_now_add=True, blank=True),
    note            = models.CharField(max_length=100)