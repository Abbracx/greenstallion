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
    monthly_salary      = models.IntegerField(default=0)
    monthly_salary_word = models.TextField(max_length=300, null=True)
    bank_name           = models.CharField(max_length=100)  
    account_number      = models.IntegerField(null=True)
    account_name        = models.CharField(max_length=100)
    bvn                 = models.IntegerField(null=True)
    loan_eligible       = models.IntegerField(null=True)
    category_max_tenure = models.PositiveSmallIntegerField(default=6)

    
    def get_halve_income(self, income=0):
        if income > 0:
            return income / 2
        return income

    def eligible_loan(self, income=None):
        if income is not None:
            return self.get_halve_income(income) * self.category_max_tenure
        return 0

    def set_eligible_loan(self,income, *args, **kwargs):
        self.loan_eligible = self.eligible_loan(income)
    
    


class BusinessOwners(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    company_name    = models.CharField(max_length=100)
    cac_number      = models.CharField(max_length=100)
    official_email  = models.EmailField()
    bank_name       = models.CharField(max_length=100)
    account_number  = models.CharField(max_length=100)
    account_name    = models.CharField(max_length=100)
    bvn             = models.IntegerField(null=True)
    monthly_salary      = models.IntegerField(default=0)
    loan_eligible       = models.IntegerField(null=True)
    category_max_tenure = models.PositiveSmallIntegerField(default=5)


    def get_halve_income(self, income=0):
        if income > 0:
            return income / 2
        return income

    def eligible_loan(self, income=None):
        if income is not None:
            return self.get_halve_income(income) * self.category_max_tenure
        return 0

    def set_eligible_loan(self,income, *args, **kwargs):
        self.loan_eligible = self.eligible_loan(income)

class BusinessOwnersDirectors(models.Model):
    user                    = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    name_of_director        = models.CharField(max_length=100)
    director_address        = models.CharField(max_length=100)
    means_of_identification = models.CharField(max_length=100)


class Corpers(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    state_code      = models.CharField(null=True,max_length=20)
    nysc_id         = models.ImageField(upload_to='pics_upload')
    validity_date   = models.DateField(null=True,max_length=100)
    lga             = models.CharField(null=True,max_length=100)
    bank_name       = models.CharField(null=True,max_length=100)
    account_number  = models.IntegerField(null=True)
    account_name    = models.CharField(null=True,max_length=100)
    bvn             = models.IntegerField(null=True)
    monthly_salary      = models.IntegerField(null=True,default=0)
    loan_eligible       = models.IntegerField(null=True)
    category_max_tenure = models.PositiveSmallIntegerField(null=True,default=4)


    def get_halve_income(self, income=0):
        if income > 0:
            return income / 2
        return income

    def eligible_loan(self, income=None):
        if income is not None:
            return self.get_halve_income(income) * self.category_max_tenure
        return 0

    def set_eligible_loan(self,income, *args, **kwargs):
        self.loan_eligible = self.eligible_loan(income)


class StallionSmart(models.Model):
    salary_earner   = models.ForeignKey(SalaryEarners, on_delete=models.CASCADE)
    type_of_asset   = models.CharField(max_length=100)
    asset_name      = models.CharField(max_length=100)
    vendor_name     = models.CharField(max_length=100)
    invoice_value   = models.IntegerField(null=True)
    loan_amount     = models.IntegerField(null=True)
    purpose_of_loan = models.TextField(null=True)


class StallionLoans(models.Model):
    salary_earner            = models.ForeignKey(SalaryEarners, on_delete=models.CASCADE)
    loan_amount     = models.IntegerField(null=True)
    purpose_of_loan = models.TextField(null=True)

class StallionAdvance(models.Model):
    salary_earner   = models.ForeignKey(SalaryEarners, on_delete = models.CASCADE)
    loan_amount     = models.IntegerField(null=True)
    purpose_of_loan = models.TextField(null=True)

class StallionFees(models.Model):
    salary_earner   = models.ForeignKey(SalaryEarners, on_delete=models.CASCADE)
    school_name     = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100)
    fees_amount     = models.IntegerField(null=True)
    loan_amount     = models.IntegerField(null=True)
    purpose_of_loan = models.TextField(null=True)

class StallionAllowee(models.Model):
    corper          = models.ForeignKey(Corpers, on_delete=models.CASCADE)
    loan_amount     = models.IntegerField(null=True)
    purpose_of_loan = models.CharField(max_length=100)
   

class StallionSupport(models.Model):
    business_owner      = models.ForeignKey(BusinessOwners, on_delete=models.CASCADE)
    business_type       = models.CharField(max_length=100)
    source_of_funds     = models.CharField(max_length=100)
    years_in_business   = models.CharField(max_length=100)
    monthly_turnover_words = models.CharField(max_length=300)
    loan_amount         = models.IntegerField(null=True)
    purpose_of_loan     = models.TextField(null=True)

   

class LoanAccount (models.Model):
    user                = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT)
    user_category       = models.CharField(max_length=200, null=True, blank=True)
    total_disbursable   = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    total_payable       = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    processing_fee_amount= models.DecimalField(max_digits=15, decimal_places=3, default=0)
    loan_amount         = models.IntegerField(null=True)
    purpose_of_loan     = models.TextField(null=True)
    loan_tenure         = models.CharField(max_length=100, null=True)
    charged_loan_interest= models.DecimalField(max_digits=15, decimal_places=3, default=0)
    package_list        = models.CharField(max_length=200, null=True)
    loan_approval       = models.BooleanField(default=None)
    loan_disbursement   = models.NullBooleanField()
    loan_repayment      = models.BooleanField(default=False)
    disbursement_date   = models.DateField(null=True)
    

    def __str__(self):
        return "Name: {0} {1}\nCategory: {2}\nPakage: {3}".format(self.user.first_name,self.user.last_name,self.user_category,self.package_list,)

    def save(self, *args, **kwargs):
        if self.loan_disbursement == True:
            self.disbursement_date = date.today()
            self.charged_loan_interest = self.get_loan_interest()
            self.processing_fee_amount = self.processing_fee()
        super(LoanAccount,self).save(*args,**kwargs)

    #loan interest
    def get_loan_interest(self, rate=None):
        DEFAULT_RATE = 5
        if rate is not None:
            return rate * 0.01
        return DEFAULT_RATE * 0.01
     
    def get_loan_halve_interest(self):
        return self.get_loan_interest() / 2

    # amount for loan interest
    def get_loan_interest_amount(self):
        return self.get_loan_interest() * self.loan_amount

    # amount for halve loan interest
    def get_loan_halve_interest_amount(self):
        return self.get_loan_halve_interest() * self.loan_amount

    def processing_fee(self, fee = None):
        DEFAULT_FEE = 2 
        if fee is not None:
            return self.loan_amount * (fee * 0.01)
        return self.loan_amount * (DEFAULT_FEE * 0.01)
    
    def set_disbursable_amount(self):
        MAX_DATE = 15
        if self.loan_disbursement == True and self.disbursement_date.day < MAX_DATE:
            self.total_disbursable = self.loan_amount - self.processing_fee_amount
        elif self.loan_disbursement == True and self.disbursement_date.day > MAX_DATE:
            self.total_disbursable = self.loan_amount - (self.processing_fee_amount + self.get_loan_halve_interest_amount())
        return 0
    
    def set_totalpayable_amount(self):
        self.total_payable = self.loan_amount + self.get_loan_interest_amount()

class Approval (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT)
    loan_approval = models.NullBooleanField ()
    loan_disbursement = models.NullBooleanField()
    loan_repayment = models.BooleanField(default=False)

