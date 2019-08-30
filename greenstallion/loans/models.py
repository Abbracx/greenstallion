import datetime
from datetime import date

from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class salary_earners(models.Model):
    user = models.ForeignKey (settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT)
    occupation = models.CharField(max_length=100)
    employment_status = models.CharField(max_length=100)
    employer_name = models.CharField(max_length=100)
    work_duration = models.CharField(max_length=100)
    office_address = models.CharField(max_length=100)
    official_email = models.EmailField()
    monthly_salary = models.IntegerField()
    monthly_salary_words = models.TextField(max_length=300)
    bank_name = models.CharField(max_length=100)
    account_number = models.IntegerField()
    account_name = models.CharField(max_length=100)
    bvn = models.IntegerField()


class business_owners(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT)
    company_name = models.CharField(max_length=100)
    cac_number = models.CharField(max_length=100)
    official_email = models.EmailField()
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    account_name = models.CharField(max_length=100)
    bvn = models.IntegerField()

class business_owners_directors(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT)
    name_of_director = models.CharField(max_length=100)
    director_address = models.CharField(max_length=100)
    means_of_identification = models.CharField(max_length=100)


class corpers(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT)
    state_code = models.CharField(max_length=20)
    nysc_id = models.ImageField('pics_upload')
    validity_date = models.DateField(max_length=100)
    lga = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    account_number = models.IntegerField()
    account_name = models.CharField(max_length=100)
    bvn = models.IntegerField()


class stallion_smart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT)
    type_of_asset = models.CharField(max_length=100)
    asset_name = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=100)
    invoice_value = models.IntegerField()
    loan_amount =models.IntegerField()

class stallion_loans(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT)
    loan_amount = models.IntegerField()
    purpose_of_loan = models.TextField()

class stallion_advance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT)
    loan_amount = models.IntegerField()
    purpose_of_loan = models.TextField()

class stallion_fees(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT)
    school_name = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100)
    fees_amount = models.IntegerField()
    loan_amount = models.IntegerField()

class stallion_allowee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT)
    loan_amount = models.IntegerField()
    purpose_of_loan = models.CharField(max_length=100)

class stallion_support(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT)
    business_type = models.CharField(max_length=100)
    source_of_funds = models.CharField(max_length=100)
    years_in_business = models.CharField(max_length=100)
    monthly_turnover = models.IntegerField()
    monthly_turnover_words = models.CharField(max_length=300)
    purpose_of_loan = models.CharField(max_length=100)
    loan_amount = models.IntegerField()
    loan_tenure = models.CharField(max_length=100)

class Categories (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    user_category = models.CharField(max_length=200, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True)
    employment_status = models.CharField(max_length=100, null=True)
    employer_name = models.CharField(max_length=100, null=True)
    work_duration = models.CharField(max_length=100, null=True)
    office_address = models.CharField(max_length=100, null=True)
    monthly_salary = models.IntegerField(null=True)
    monthly_salary_words = models.TextField(max_length=300, null=True)
    bank_name = models.CharField(max_length=100, null=True)
    account_number = models.IntegerField(null=True)
    account_name = models.CharField(max_length=100, null=True)
    bvn = models.IntegerField(null=True)
    company_name = models.CharField(max_length=100, null=True)
    cac_number = models.CharField(max_length=100, null=True)
    official_email = models.EmailField(null=True)
    name_of_director = models.CharField(max_length=100, null=True)
    director_address = models.CharField(max_length=100, null=True)
    means_of_identification = models.CharField(max_length=100, null=True)
    state_code = models.CharField(max_length=20, null=True)
    nysc_id = models.ImageField('pics', null=True)
    validity_date = models.DateField(null=True)
    lga = models.CharField(max_length=100, null=True)
    type_of_asset = models.CharField(max_length=100, null=True)
    asset_name = models.CharField(max_length=100, null=True)
    vendor_name = models.CharField(max_length=100, null=True)
    invoice_value = models.IntegerField(null=True)
    loan_amount = models.IntegerField(null=True)
    purpose_of_loan = models.TextField(null=True)
    school_name = models.CharField(max_length=100, null=True)
    education_level = models.CharField(max_length=100, null=True)
    fees_amount = models.IntegerField(null=True)
    business_type = models.CharField(max_length=100, null=True)
    source_of_funds = models.CharField(max_length=100, null=True)
    years_in_business = models.CharField(max_length=100, null=True)
    monthly_turnover = models.IntegerField(null=True)
    monthly_turnover_words = models.CharField(max_length=300, null=True)
    loan_tenure = models.CharField(max_length=100, null=True)
    package_list = models.CharField(max_length=200, null=True)
    loan_approval = models.NullBooleanField()
    loan_disbursement = models.NullBooleanField()
    loan_repayment = models.BooleanField(default=False)
    disbursement_date = models.DateTimeField(auto_now=True)
    allowee = models.IntegerField(null=True)


class LoanPackages(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT)
    type_of_asset = models.CharField(max_length=100, null=True)
    asset_name = models.CharField(max_length=100, null=True)
    vendor_name = models.CharField(max_length=100, null=True)
    invoice_value = models.IntegerField(null=True)
    loan_amount = models.IntegerField(null=True)
    purpose_of_loan = models.TextField(null=True)
    school_name = models.CharField(max_length=100, null=True)
    education_level = models.CharField(max_length=100, null=True)
    fees_amount = models.IntegerField(null=True)
    business_type = models.CharField(max_length=100, null=True)
    source_of_funds = models.CharField(max_length=100, null=True)
    years_in_business = models.CharField(max_length=100, null=True)
    monthly_turnover = models.IntegerField(null=True)
    monthly_turnover_words = models.CharField(max_length=300, null=True)
    loan_tenure = models.CharField(max_length=100, null=True)


class Approval (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT)
    loan_approval = models.NullBooleanField ()
    loan_disbursement = models.NullBooleanField()
    loan_repayment = models.BooleanField(default=False)

