import datetime
from datetime import date,timedelta

from django.db import models
from django.conf import settings
from django.utils import timezone
from loans.models import LoanAccount
from accounts.models import User, Profile
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404




# Create your models here.


class RepaymentAccount(models.Model):
    applied          = models.BooleanField(default=False)
    repaid           = models.BooleanField(default=False)
    monthly_repaid      = models.BooleanField(default=False)
    lateness            = models.BooleanField(default=False)
    loan_owed           = models.DecimalField(max_digits=15, decimal_places=3,null=True)
    paid_amount         = models.DecimalField(max_digits=15, decimal_places=3,null=True)
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


    def set_monthly_payment(self):
        self.per_monthly_payment = float(self.loan_owed) / float(self.user_loan.loan_tenure)
    
    def check_for_lateness(self, today): 
        if not self.is_monthly_repaid():
            if today > self.lateness_date:
                self.lateness_fee = self.user_loan.loan_amount * self.get_lateness_rate()
                self.lateness = True
                super(RepaymentAccount,self).save()

    def get_lateness_rate(self, rate=None):
        DEFAULT_RATE = 2
        if rate is not None:
            return rate * 0.01
        return DEFAULT_RATE * 0.01

    
    def is_applied(self):
        return self.applied
    
    def is_repaid(self):
        return self.repaid
    
    def is_monthly_repaid(self):
        return self.monthly_repaid
    
    def is_lateness(self):
        return self.lateness
