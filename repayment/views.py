from django.shortcuts import render
from .models import RepaymentAccount
from .models import PayStackDetails
from loans.models import LoanAccount
from accounts.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from datetime import date, timedelta
from django.db.models import Q
from django.http import HttpResponse
from paystackapi.transaction import Transaction
import string
import random

# Create your views here.
def repayment (request):
    outstanding = RepaymentAccount.objects.filter(Q(repaid=False) & Q(user_loan__loan_disbursement=True)).select_related('user_loan')
    return render(request, 'repayment/data.html', {'outstanding': outstanding})

def client_repayment_history(request, id):

    history = RepaymentAccount.objects.select_related('user_loan').get(user_loan__user=id)

    return render(request, 'repayment/client_data.html', {'history': history})

def initiate_card_first_transaction(request, id):

    user = get_object_or_404(User, pk=id)
    response = None
    VERIFICATION_AMOUNT = 1000
    REF_LENGTH = 16

    if user.is_active:
        ref = ''.join([random.choice(string.ascii_lowercase + string.digits) 
                        for _ in range(REF_LENGTH)])
        response = Transaction.initialize(reference=ref, amount=VERIFICATION_AMOUNT, email=user.email, callback_url='http://127.0.0.1:8000/repayment/card-verified')
        if response:
            return redirect(response['data'].get('authorization_url'))
        else:
            return HttpResponse('Oops! Something bad happened.')
    
        
def verify_card_payment(request):
    
    reference  = request.GET['reference']
    
    verify_transaction = Transaction.verify(reference=reference)
    auth_code          = verify_transaction['data']['authorization'].get('authorization_code')
    signature_code     = verify_transaction['data']['authorization'].get('signature')
    is_reusable        = verify_transaction['data']['authorization'].get('reusable')

    if is_reusable:
        PayStackDetails.objects.create(auth_code= auth_code, 
                                       signature_code= signature_code,
                                       user= request.user)
        return redirect('user_bank_statement', request.user.id)
    return redirect('apply_loan', request.user.id)
        


def make_payment(request, id):

    try:
        repayment_obj = RepaymentAccount.objects.get(user_loan__user = id)
        user = User.objects.get(pk=id)
        paystack= PayStackDetails.objects.get(user__id = id)
    except ObjectDoesNotExist:
         pass
    else:
        if request.method == "POST":
            paid_amount = request.POST.get('amount')
            if paid_amount:
                #create ref code
                REF_LENGTH = 16
                ref = ''.join([random.choice(string.ascii_lowercase + string.digits) for _ in range(REF_LENGTH)])
                response = Transaction.charge(reference=ref, authorization_code=paystack.auth_code,
                                             amount=paid_amount, email=user.email)
                if response:
                    #claculate the loan still owing
                    repayment_obj.loan_owed = float(repayment_obj.loan_owed) -  float(response['data'].get('amount'))

                    repayment_obj.paid_amount = float(repayment_obj.paid_amount) - float(paid_amount)
                    repayment_obj.save()

    
        '''
        if obj.loan_owed is > 0:
            if not obj:
                obj.lateness_days += 1
                obj.save()
        
                user_loan_details.total_payable = user_loan_details.total_payable + latenessInterest(per_monthly_payment,rate)   
                    
            if obj.monthly_repaid and date.today() < obj.lateness_date:
                user_loan_details.total_payable = user_loan_details.total_payable - payment
                
            NEXT_PAYMENT_DATE = NEXT_PAYMENT_DATE + timedelta(days = 30)
        else:
            LOAN_REPAID = True

    def get_monthly_amount(per_monthly_amount):
        paid = False
        amount = 0
        if amount_from_gateway == per_monthly_amount:
            paid = True
            amount = amount_from_gateway
            return {'paid': True, 'amount': amount}
    return {'paid':paid, 'amount':amount}
                
        
    def latenessInterest(monthly_repayment,rate):
        return monthly_repayment * (rate/100)

'''
    return render(request,'payment.html',{'repayment_details':repayment_obj})
    
'''
def loan_disbursement_loan(request):
    loan_calculator = request.POST.get('loan_calculator',"")
    loan_eligible = request.POST.get('loan_eligible',"")
    loan_half_interest_amount = request.POST.get('loan_half_interest_amount',"")
    processing_fee_amount = request.POST.get('processing_fee_amount',"")
    loan_tenure = request.Category.loan_tenure
    max_tenure = request.POST.get ('max_tenure',"")
    loan_amount = request.Category.loan_amount
    loan_interest_amount = request.POST.get('loan_interest_amount',"")
    loan_interest = request.POST.get ('loan_interest',"")
    loan_disbursement_date = request.Category.disbursement_date
    total_payable = request.POST.get('total_payable',"")
    total_disbursable = request.POST.get ('total_disbursable',"")
    loan_half_interest = request.POST.get('loan_half_interest',"")
    processing_fee = request.POST.get('processing_fee', "")
    repayment_date = request.POST.get('repayment_date',"")

    if loan_calculator:
        loan_calculator = income / 2

    if loan_eligible:
        loan_eligible = loan_calculator * max_tenure

    if loan_half_interest_amount:
        loan_half_interest_amount = loan_amount * loan_half_interest

    if processing_fee_amount:
        processing_fee_amount = loan_amount * processing_fee

    if loan_tenure <= max_tenure and loan_amount <= loan_eligible:
        loan_interest_amount = (loan_interest * loan_amount) * loan_tenure
        loan_disbursement_date = loan_disbursement_date

    if total_payable:
        total_payable = loan_interest_amount + loan_amount

    if repayment_date and (loan_disbursement_date = range 1-14th): # we are to count repayment calendar here
        repayment_date = repayment_date
    else:
        repayment_date = repayment_date + 30 days

    if total_disbursable and loan_disbursement_date = range 1-14th:
        total_disbursable = loan_amount - processing_fee_amount
    else:
        total_disbursable = loan_amount - (processing_fee_amount + loan_half_interest_amount)


def LoanRepayment(request):
    number_lateness_days = request.POST.get('number_lateness_days',"")
    monthly_payment = request.POST.get('monthly_payment',"")
    lateness_fee_amount = request.POST.get('lateness_fee_amount',"")
    monthly_lateness_fee = request.POST.get('monthly_lateness_fee',"")
    monthly_due = request.POST.get('monthly_due',"")
    next_due = request.POST.get('next_due',"")
    total_payable = request.POST.get('total_payable', "")
    loan_tenure = request.Category.loan_tenure
    lateness_fee = request.POST.get('lateness_fee', "")
    loan_amount = request.Category.loan_amount
    payment = request.POST.get('payment',"")
    paid = request.POST.get('paid', "")

    if number_lateness_days:
        number_lateness_days = len[number of days that “loan_repayment = false” from repayment_date]

    if monthly_payment:
        monthly_payment = total_payable / loan_tenure

    if lateness_fee_amount:
        lateness_fee_amount= lateness_fee * loan_amount

    if monthly_lateness_fee:
        monthly_lateness_fee = lateness_fee_amount * number_lateness_days

    if monthly_due:
        monthly_due = monthly_lateness_fee + monthly_payment

    if next_due and payment = True and paid == montly_due:
        next_due = total_payable - monthly_due
    elif paid < monthly_due:
        next_due = total_payable - paid
    else:
        next_due =
'''