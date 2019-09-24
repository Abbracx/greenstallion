import datetime
from datetime import date

from django.db import models
from django.conf import settings
from django.utils import timezone
from loans.models import LoanAccount
from accounts.models import User, Profile



# Create your models here.


class RepaymentAccount(models.Model):
    loan_applied        = models.BooleanField(default=False)
    loan_repaid         = models.BooleanField(default=False)
    monthly_repaid      = models.BooleanField(default=False)
    lateness            = models.BooleanField(default=False)
    loan_owed           = models.DecimalField(max_digits=15, decimal_places=3,null=True)
    per_monthly_payment = models.DecimalField(max_digits=15, decimal_places=3,null=True)
    lateness_fee        = models.DecimalField(max_digits=15, decimal_places=3,null=True)
    max_loan_tenure     = models.PositiveSmallIntegerField(null=True)
    user_loan_tenure    = models.PositiveSmallIntegerField(null=True)
    next_payment_date   = models.DateField(null=True)
    lateness_date       = models.DateField(null=True)
    repayment_date      = models.DateField(null=True)
    loan_interest       = models.IntegerField(null=True)
    loan_disbursed      = models.BooleanField()
    user_loan           = models.ForeignKey(LoanAccount, on_delete= models.CASCADE)

    
    