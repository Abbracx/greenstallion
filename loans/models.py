import datetime
from datetime import date

from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class SalaryEarners(models.Model):
    user                = models.ForeignKey (settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    occupation          = models.CharField(max_length=100)
    employment_status   = models.CharField(max_length=100)
    employer_name       = models.CharField(max_length=100)
    work_duration       = models.CharField(max_length=100)
    office_address      = models.CharField(max_length=100)
    official_email      = models.EmailField()
    monthly_salary      = models.IntegerField()
    monthly_salary_word = models.TextField(max_length=300, null=True)
    bank_name           = models.CharField(max_length=100)
    account_number      = models.IntegerField()
    account_name        = models.CharField(max_length=100)
    bvn                 = models.IntegerField()
    


class BusinessOwners(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    company_name    = models.CharField(max_length=100)
    cac_number      = models.CharField(max_length=100)
    official_email  = models.EmailField()
    bank_name       = models.CharField(max_length=100)
    account_number  = models.CharField(max_length=100)
    account_name    = models.CharField(max_length=100)
    bvn             = models.IntegerField()

class BusinessOwnersDirectors(models.Model):
    user                    = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    name_of_director        = models.CharField(max_length=100)
    director_address        = models.CharField(max_length=100)
    means_of_identification = models.CharField(max_length=100)


class Corpers(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    state_code      = models.CharField(max_length=20)
    nysc_id         = models.ImageField(upload_to='pics_upload')
    validity_date   = models.DateField(max_length=100)
    lga             = models.CharField(max_length=100)
    bank_name       = models.CharField(max_length=100)
    account_number  = models.IntegerField()
    account_name    = models.CharField(max_length=100)
    bvn             = models.IntegerField()


class StallionSmart(models.Model):
    salary_earner   = models.ForeignKey(SalaryEarners, on_delete=models.CASCADE)
    type_of_asset   = models.CharField(max_length=100)
    asset_name      = models.CharField(max_length=100)
    vendor_name     = models.CharField(max_length=100)
    invoice_value   = models.IntegerField()
    loan_amount     = models.IntegerField()

class StallionLoans(models.Model):
    salary_earner            = models.ForeignKey(SalaryEarners, on_delete=models.CASCADE)
    loan_amount     = models.IntegerField()
    purpose_of_loan = models.TextField()

class StallionAdvance(models.Model):
    salary_earner   = models.ForeignKey(SalaryEarners, on_delete = models.CASCADE)
    loan_amount     = models.IntegerField()
    purpose_of_loan = models.TextField()

class StallionFees(models.Model):
    salary_earner   = models.ForeignKey(SalaryEarners, on_delete=models.CASCADE)
    school_name     = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100)
    fees_amount     = models.IntegerField()
    loan_amount     = models.IntegerField()

class StallionAllowee(models.Model):
    corper          = models.ForeignKey(Corpers, on_delete=models.CASCADE)
    loan_amount     = models.IntegerField()
    purpose_of_loan = models.CharField(max_length=100)
    package_list    = models.CharField(max_length=100)
    allowee         = models.IntegerField()

class StallionSupport(models.Model):
    business_owner      = models.ForeignKey(BusinessOwners, on_delete=models.CASCADE)
    business_type       = models.CharField(max_length=100)
    source_of_funds     = models.CharField(max_length=100)
    years_in_business   = models.CharField(max_length=100)
    monthly_turnover    = models.IntegerField()
    monthly_turnover_words = models.CharField(max_length=300)
    purpose_of_loan     = models.CharField(max_length=100)
    loan_amount         = models.IntegerField()
    loan_tenure         = models.CharField(max_length=100)

class LoanAccount (models.Model):
    user                = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT)
    user_category       = models.CharField(max_length=200, null=True, blank=True)
    loan_amount         = models.IntegerField(null=True)
    purpose_of_loan     = models.TextField(null=True)
    loan_tenure         = models.CharField(max_length=100, null=True)
    package_list        = models.CharField(max_length=200, null=True)
    monthly_income      = models.IntegerField(null=True)
    loan_approval       = models.BooleanField(default=None, null=True)
    loan_disbursement   = models.NullBooleanField()
    loan_repayment      = models.BooleanField(default=False)
    disbursement_date   = models.DateField(null=True)

    def __str__(self):
        return self.user.first_name

    def save(self, *args, **kwargs):
        if self.loan_disbursement == True:
            self.disbursement_date = date.today()
        super(LoanAccount,self).save(*args,**kwargs)
    


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

