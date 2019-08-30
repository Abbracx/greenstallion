import datetime
from datetime import date

from django.db import models
from django.conf import settings
from django.utils import timezone



# Create your models here.


class RepaymentManagement(models.Model):
    max_tenure = models.IntegerField()
    loan_interest = models.IntegerField()
    category = models.ForeignKey()
    package_list = models.ForeignKey()
    lateness_fee = models.IntegerField()
    repayment_date =models.DateTimeField()
    loan_calculator = models.IntegerField()
    loan_eligibility = models.IntegerField()
    loan_tenure= models.ForeignKey()
    loan_amount = models.ForeignKey()
    total_payable = models.IntegerField()
    monthly_payment = models.IntegerField()
    total_disbursable = models.IntegerField()
    total_lateness_fee = models.IntegerField()
    monthly_due = models.IntegerField()
    total_due = models.IntegerField()
    loan_half_interest = models.IntegerField()
    loan_half_interest_amount = models.IntegerField()
    loan_interest_amount = models.IntegerField()
    loan_disbursement_date = models.ForeignKey()
    processing_fee=models.IntegerField()
    processing_fee_deduction= models.IntegerField()
    loan_repayment = models.ForeignKey()
    number_lateness_days = models.IntegerField()
    lateness_fee_amount = models.IntegerField()
    payment = models.BooleanField()
    next_payment = models.IntegerField()
    paid = models.IntegerField()
