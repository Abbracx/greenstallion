from django.shortcuts import render
from .models import RepaymentAccount
from loans.models import LoanAccount
from accounts.models import User
from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, timedelta
from django.http import HttpResponse

# Create your views here.

def create_payment_process(request, id):

    user_loan_details = get_object_or_404(LoanAccount, user__id=id)

    if user_loan_details.loan_approval==True and user_loan_details.loan_disbursement==True:
        obj = RepaymentAccount.objects.filter(user_loan=user_loan_details.id)
        if obj:
            return redirect('make_payment', id)
        else:
            obj = RepaymentAccount.objects.create(loan_applied=True, loan_disbursed=user_loan_details.loan_disbursement, user_loan=user_loan_details)
            if user_loan_details.disbursement_date.day <= 15:
                obj.repayment_date = user_loan_details.disbursement_date
                obj.loan_owed = user_loan_details.loan_amount
                obj.save()
            else:
                obj.repayment_date = user_loan_details.disbursement_date + timedelta(30)
                obj.loan_owed = user_loan_details.loan_amount
                obj.save()
        return redirect('make_payment', id)   
    
    user_loan_details = None
    return render(request,'loan_status.html',{'user_loan_details':user_loan_details})


def make_payment(request, id): 
    user_loan_details = get_object_or_404(LoanAccount, user__id=id)
    obj = RepaymentAccount.objects.filter(user_loan=user_loan_details.id)
    return render(request,'payment.html',{'repayment_details':obj})

    
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