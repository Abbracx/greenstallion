from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from .models import corpers
from .models import business_owners
from .models import salary_earners
from .models import stallion_advance
from .models import stallion_allowee
from .models import stallion_fees
from .models import stallion_loans
from .models import stallion_smart
from .models import stallion_support
from .models import business_owners_directors
from .models import Categories
from .models import LoanPackages
from .models import Approval
#from accounts.models import User

# Create your views here.

#the borrower part starts here
@login_required
def borrower_data(request):
    #fee_package = list(stallion_fees.objects.values_list('user_id', flat=True))
    #smart_package = list(stallion_smart.objects.values_list('user_id', flat=True))
    #advance_package = list(stallion_advance.objects.values_list('user_id', flat=True))
    #loans_package = list(stallion_loans.objects.values_list('user_id', flat=True))
    #support_package = list(stallion_support.objects.values_list('user_id', flat=True))
    #allowee_package = list(stallion_allowee.objects.values_list('user_id', flat=True))
    #nysc = list(corpers.objects.values_list('user_id', flat=True))
    #business = list(business_owners.objects.values_list('user_id', flat=True))
    #employees = list(salary_earners.objects.values_list('user_id', flat=True))
    #directors = list(business_owners_directors.objects.values_list('user_id', flat=True))

    #all_models = fee_package+advance_package+smart_package+loans_package+support_package+allowee_package+nysc+business+employees+directors

   # all_borrowers = User.objects.filter(id__in = all_models)
    #import pdb; pdb.set_trace()
    users = Categories.objects.all()
    return render(request, 'borrower/data.html', {"users": users})

@login_required
def borrower_pending(request):
    return render(request, 'borrower/data-active=0.html')
@login_required
def borrower_create(request):
    return render(request, 'borrower/create.html')
@login_required
def borrower_group_data(request):
    return render(request, 'borrower/group/data.html')
@login_required
def borrower_group_create(request):
    return render(request, 'borrower/group/create.html')

#the loan part starts here
@login_required
def apply_loan(request):
    if request.method == 'POST':
        salary_loan_options = request.POST.get('loan_product_id')
        if salary_loan_options == 'stallion_smart':
            return redirect('stallion_smart_loan')
        elif salary_loan_options == 'stallion_fees':
            return redirect('stallion_fees_loan')
        elif salary_loan_options == 'stallion_loans':
            return redirect('stallion_loans_loan')
        elif salary_loan_options == 'stallion_advance':
            return redirect('stallion_advance_loan')
        else:
            return render (request, 'loan/apply_loan.html')


    return render(request, 'loan/apply_loan.html')
@login_required
def loan_data(request):
    return render(request, 'loan/data.html')
@login_required
def loan_pending(request):
    pending = Categories.objects.all()
    if request.method == 'POST':
        loan_approval = request.POST.get('action')
        loan_pk = request.POST.get('pk')
        admin_decision = Categories.objects.get(pk=loan_pk)
        #import pdb; pdb.set_trace()
        if loan_approval == 'AP':
            admin_decision.loan_approval = True
            admin_decision.save()
            return redirect('loan_pending')
        elif loan_approval == 'DE':
            admin_decision.loan_approval = False
            admin_decision.save()
            return redirect('loan_pending')
        else:
            pass

        return redirect('loan_pending')

    return render(request, 'loan/data-status=pending.html', {"pending": pending})

@login_required
def loan_approved(request):
    disbursement = Categories.objects.all()
    if request.method == 'POST':
        loan_disbursement = request.POST.get('action')
        payment_pk = request.POST.get('pk')
        fund_disbursement = Categories.objects.get(pk=payment_pk)
        # import pdb; pdb.set_trace()
        if loan_disbursement == 'AP':
            fund_disbursement.loan_disbursement = True
            fund_disbursement.save()
            return redirect('loan_approved')
        elif loan_disbursement == 'DE':
            fund_disbursement.loan_disbursement = False
            fund_disbursement.save()
            return redirect('loan_approved')
        else:
            pass

        return redirect('loan_approved')

    return render(request, 'loan/data-status=approved.html',{"disbursement": disbursement})
@login_required
def loan_declined(request):
    declined = Categories.objects.all()
    return render(request, 'loan/data-status=declined.html',{"declined":declined})
@login_required
def loan_withdrawn(request):
    return render(request, 'loan/data-status=withdrawn.html')
@login_required
def loan_writtenoff(request):
    return render(request, 'loan/data-status=written_off.html')
@login_required
def loan_closed(request):
    return render(request, 'loan/data-status=closed.html')
@login_required
def loan_disbursed(request):
    disbursed = Categories.objects.all()
    return render(request, 'loan/data-status=loan_disbursed.html', {"disbursed":disbursed})
@login_required
def loan_create(request):
    return render(request, 'loan/create.html')
    
@login_required
def loan_applications(request):
    full_details = Categories.objects.all()
    return render(request, 'loan/loan_application/data.html', {"full_details":full_details})
@login_required
def loan_products(request):
    return render(request, 'loan/loan_product/data.html')
@login_required
def loan_charges(request):
    return render(request, 'charge/data.html')
@login_required
def loan_disbursedby(request):
    return render(request, 'loan/loan_disbursed_by/data.html')
@login_required
def loan_repayment_method(request):
    return render(request, 'loan/loan_repayment_method/data.html')
@login_required
def loan_provision_rate(request):
    return render(request, 'loan/provision/data.html')
@login_required
def loan_calculator(request):
    return render(request, 'loan/loan_calculator/create.html')
@login_required
def loan_guarantors(request):
    return render(request, 'guarantor/data.html')



#the collateral part starts here
@login_required
def view_collaterals(request):
    return render(request, 'collateral/data.html')
@login_required
def collateral_types(request):
    return render(request, 'collateral/type/data.html')


#the loan packages starts is here
@login_required
def stallion_advance_loan(request):
    if request.method == "POST":
        user = request.user
        first_name = request.user.first_name
        user_category = request.user.category
        last_name = request.user.last_name
        username = request.user.username
        occupation = request.POST.get('occupation', "")
        employment_status = request.POST.get('employment_status', "")
        employer_name = request.POST.get('employer_name', "")
        work_duration = request.POST.get('work_duration', "")
        office_address = request.POST.get('office_address', "")
        official_email = request.POST.get('official_email', "")
        monthly_salary = request.POST.get('monthly_salary', "")
        monthly_salary_words = request.POST.get('monthly_salary_words', "")
        bank_name = request.POST.get('bank_name', "")
        account_number = request.POST.get('account_number', "")
        account_name = request.POST.get('account_name', "")
        bvn = request.POST.get('bvn', "")
        loan_amount = request.POST.get('loan_amount', "")
        purpose_of_loan = request.POST.get('purpose_of_loan', "")
        package_list = request.POST.get('package_list', "")
        loan_approval = request.POST.get('loan_approval', "")
        loan_disbursement = request.POST.get('loan_disbursement',"")
        loan_repayment = request.POST.get('loan_repayment',"")
        #import pdb; pdb.set_trace()
        if bvn:
            bvn= int(bvn)
        if monthly_salary:
            monthly_salary = int(monthly_salary)
        if loan_amount:
            loan_amount = int(loan_amount)
        if account_number:
            account_number= int(account_number)


        salary_earners_info = Categories.objects.create(occupation=occupation, employment_status=employment_status, employer_name=employer_name, work_duration=work_duration,
                                          office_address=office_address, official_email=official_email, monthly_salary=monthly_salary,
                                          monthly_salary_words=monthly_salary_words, bank_name=bank_name, account_number= account_number, account_name = account_name,
                                          bvn=bvn, user= user, first_name=first_name, last_name=last_name, username=username, user_category=user_category, loan_amount=loan_amount,
                                          purpose_of_loan=purpose_of_loan, package_list=package_list, loan_approval=loan_approval, loan_disbursement=loan_disbursement, loan_repayment=loan_repayment)
        #stallion_advance_details = LoanPackages.objects.create(loan_amount=loan_amount, purpose_of_loan=purpose_of_loan, user=user)
        salary_earners_info.save()
        #stallion_advance_details.save()
        print('Loan Application Successful')
        return redirect('stallion_advance_loan')
    return render(request, 'loan/stallion_advance_form.html')
@login_required
def stallion_allowee_loan(request):
    if request.method == "POST":
        user = request.user
        first_name = request.user.first_name
        user_category = request.user.category
        last_name = request.user.last_name
        username = request.user.username
        state_code = request.POST.get('state_code', "")
        nysc_id = request.POST.get('nysc_id', "")
        validity_date = request.POST.get('validity_date', "")
        lga = request.POST.get('lga', "")
        bank_name = request.POST.get('bank_name', "")
        account_number = request.POST.get('account_number', "")
        account_name = request.POST.get('account_name', "")
        bvn = request.POST.get('bvn', "")
        loan_amount = request.POST.get('loan_amount', "")
        purpose_of_loan = request.POST.get('purpose_of_loan', "")
        package_list = request.POST.get('package_list', "")
        allowee=request.POST.get('allowee',"")

        if account_number:
            account_number= int(account_number)

        if bvn:
            bvn= int(bvn)
        if loan_amount:
            loan_amount= int(loan_amount)
        if allowee:
            allowee =int(allowee)

        corpers_info = Categories.objects.create(state_code=state_code, nysc_id=nysc_id, validity_date=validity_date,lga=lga,
                                                            bank_name=bank_name, account_number=account_number,
                                                            account_name=account_name,
                                                            bvn=bvn, user=user,first_name=first_name, last_name=last_name, username=username, user_category=user_category,
                                                 loan_amount=loan_amount,purpose_of_loan=purpose_of_loan, package_list=package_list, allowee=allowee)
        #stallion_allowee_details = LoanPackages.objects.create(loan_amount=loan_amount,purpose_of_loan=purpose_of_loan, user=user)
        corpers_info.save();
        #stallion_allowee_details.save();
        print('Loan Application Successful')
        return redirect('stallion_allowee_loan')
    return render(request, 'loan/stallion_allowee_form.html')

@login_required
def stallion_support_loan(request):
    if request.method == "POST":
        user = request.user
        first_name = request.user.first_name
        user_category = request.user.category
        last_name = request.user.last_name
        username = request.user.username
        company_name = request.POST.get('company_name', "")
        cac_number = request.POST.get('cac_number', "")
        official_email = request.POST.get('official_email', "")
        bank_name = request.POST.get('bank_name', "")
        account_number = request.POST.get('account_number', "")
        account_name = request.POST.get('account_name', "")
        bvn = request.POST.get('bvn', "")
        name_of_director = request.POST.get('name_of_director', "")
        director_address = request.POST.get('director_address', "")
        means_of_identification = request.POST.get('means_of_identification', "")
        business_type = request.POST.get('business_type', "")
        source_of_funds = request.POST.get('source_of_funds', "")
        years_in_business = request.POST.get('years_in_business', "")
        monthly_turnover = request.POST.get('monthly_turnover', "")
        monthly_turnover_words = request.POST.get('monthly_turnover_words', "")
        purpose_of_loan = request.POST.get('purpose_of_loan', "")
        loan_amount = request.POST.get('loan_amount', "")
        loan_tenure = request.POST.get('loan_tenure', "")
        package_list = request.POST.get('package_list', "")

        if monthly_turnover:
            monthly_turnover = int(monthly_turnover)

        if loan_amount:
            loan_amount = int (loan_amount)

        if bvn:
            bvn = int(bvn)

        business_owner_info = Categories.objects.create(company_name=company_name,cac_number=cac_number,official_email=official_email, bank_name=bank_name,
                                                             account_number=account_number, account_name=account_name, bvn=bvn, name_of_director=name_of_director,
                                                        director_address=director_address, means_of_identification=means_of_identification, user=user,
                                                        first_name=first_name, last_name=last_name, username=username, user_category=user_category, package_list=package_list,business_type=business_type,source_of_funds=source_of_funds, years_in_business=years_in_business,
                                                                   monthly_turnover=monthly_turnover, monthly_turnover_words=monthly_turnover_words, purpose_of_loan=purpose_of_loan,
                                                                   loan_amount=loan_amount, loan_tenure=loan_tenure)
        #stallion_support_details = LoanPackages.objects.create(business_type=business_type,source_of_funds=source_of_funds, years_in_business=years_in_business,monthly_turnover=monthly_turnover, monthly_turnover_words=monthly_turnover_words, purpose_of_loan=purpose_of_loan,loan_amount=loan_amount, loan_tenure=loan_tenure, user=user)
        business_owner_info.save();
        #stallion_support_details.save();
        print('Loan Application Successful')
        return redirect('stallion_support_loan')
    return render(request, 'loan/stallion_support_form.html')

@login_required
def stallion_fees_loan(request):
    if request.method == "POST":
        user = request.user
        first_name = request.user.first_name
        user_category = request.user.category
        last_name = request.user.last_name
        username = request.user.username
        occupation = request.POST.get('occupation', "")
        employment_status = request.POST.get('employment_status', "")
        employer_name = request.POST.get('employer_name', "")
        work_duration = request.POST.get('work_duration', "")
        office_address = request.POST.get('office_address', "")
        official_email = request.POST.get('official_email', "")
        monthly_salary = request.POST.get('monthly_salary', "")
        monthly_salary_words = request.POST.get('monthly_salary_words', "")
        bank_name = request.POST.get('bank_name', "")
        account_number = request.POST.get('account_number', "")
        account_name = request.POST.get('account_name', "")
        bvn = request.POST.get('bvn', "")
        school_name = request.POST.get('school_name', "")
        education_level = request.POST.get('education_level', "")
        fees_amount = request.POST.get('fees_amount', "")
        loan_amount = request.POST.get('bvn', "")
        package_list = request.POST.get('package_list', "")
        if bvn:
            bvn= int(bvn)
        if monthly_salary:
            monthly_salary = int(monthly_salary)
        if loan_amount:
            loan_amount = int(loan_amount)
        if account_number:
            account_number= int(account_number)
        if fees_amount:
            fees_amount= int(fees_amount)

        salary_earners_info = Categories.objects.create(occupation=occupation, employment_status=employment_status, employer_name=employer_name, work_duration=work_duration,
                                          office_address=office_address, official_email=official_email, monthly_salary=monthly_salary,
                                          monthly_salary_words=monthly_salary_words, bank_name=bank_name, account_number= account_number, account_name = account_name,
                                          bvn=bvn, user=user, first_name=first_name, last_name=last_name, username=username, user_category=user_category, package_list=package_list,
                                                        school_name=school_name, education_level=education_level, fees_amount=fees_amount, loan_amount=loan_amount)
        #stallion_fees_details = LoanPackages.objects.create(school_name=school_name, education_level=education_level, fees_amount=fees_amount, loan_amount=loan_amount, user=user)
        salary_earners_info.save();
        #stallion_fees_details.save();
        print('Loan Application Successful')
        return redirect('stallion_fees_loan')
    return render(request, 'loan/stallion_fees_form.html')

@login_required
def stallion_loans_loan(request):
    if request.method == "POST":
        user = request.user
        first_name = request.user.first_name
        user_category = request.user.category
        last_name = request.user.last_name
        username = request.user.username
        occupation = request.POST.get('occupation', "")
        employment_status = request.POST.get('employment_status', "")
        employer_name = request.POST.get('employer_name', "")
        work_duration = request.POST.get('work_duration', "")
        office_address = request.POST.get('office_address', "")
        official_email = request.POST.get('official_email', "")
        monthly_salary = request.POST.get('monthly_salary', "")
        monthly_salary_words = request.POST.get('monthly_salary_words', "")
        bank_name = request.POST.get('bank_name', "")
        account_number = request.POST.get('account_number', "")
        account_name = request.POST.get('account_name', "")
        bvn = request.POST.get('bvn', "")
        loan_amount = request.POST.get('loan_amount', "")
        purpose_of_loan = request.POST.get('purpose_of_loan', "")
        package_list = request.POST.get('package_list', "")
        #import pdb; pdb.set_trace()
        if bvn:
            bvn = int(bvn)
        if monthly_salary:
            monthly_salary = int(monthly_salary)
        if loan_amount:
            loan_amount = int(loan_amount)
        if account_number:
            account_number = int(account_number)



        salary_earners_info = Categories.objects.create(occupation=occupation, employment_status=employment_status, employer_name=employer_name, work_duration=work_duration,
                                          office_address=office_address, official_email=official_email, monthly_salary=monthly_salary,
                                          monthly_salary_words=monthly_salary_words, bank_name=bank_name, account_number= account_number, account_name = account_name,
                                          bvn=bvn, user=user,first_name=first_name, last_name=last_name, username=username, user_category=user_category,
                                                        loan_amount=loan_amount, purpose_of_loan=purpose_of_loan, package_list=package_list)
        #stallion_loans_details = LoanPackages.objects.create(loan_amount=loan_amount, purpose_of_loan=purpose_of_loan, user=user)
        salary_earners_info.save();
        #stallion_loans_details.save();
        print('Loan Application Successful')
        return redirect('stallion_loans_loan')
    return render(request, 'loan/stallion_loans_form.html')

@login_required
def stallion_smart_loan(request):
    if request.method == "POST":
        user = request.user
        first_name = request.user.first_name
        user_category = request.user.category
        last_name = request.user.last_name
        username = request.user.username
        occupation = request.POST.get('occupation', "")
        employment_status = request.POST.get('employment_status', "")
        employer_name = request.POST.get('employer_name', "")
        work_duration = request.POST.get('work_duration', "")
        office_address = request.POST.get('office_address', "")
        official_email = request.POST.get('official_email', "")
        monthly_salary = request.POST.get('monthly_salary', "")
        monthly_salary_words = request.POST.get('monthly_salary_words', "")
        bank_name = request.POST.get('bank_name', "")
        account_number = request.POST.get('account_number', "")
        account_name = request.POST.get('account_name', "")
        bvn = request.POST.get('bvn', "")
        type_of_asset = request.POST.get('type_of_asset', "")
        asset_name = request.POST.get('asset_name', "")
        vendor_name = request.POST.get('vendor_name', "")
        invoice_value = request.POST.get('invoice_value', "")
        loan_amount = request.POST.get('loan_amount', "")
        package_list = request.POST.get('package_list', "")
        if bvn:
            bvn= int(bvn)
        if monthly_salary:
            monthly_salary = int(monthly_salary)
        if loan_amount:
            loan_amount = int(loan_amount)
        if account_number:
            account_number= int(account_number)


        salary_earners_info = Categories.objects.create(occupation=occupation, employment_status=employment_status, employer_name=employer_name, work_duration=work_duration,
                                          office_address=office_address, official_email=official_email, monthly_salary=monthly_salary,
                                          monthly_salary_words=monthly_salary_words, bank_name=bank_name, account_number= account_number, account_name = account_name,
                                          bvn=bvn, user=user, first_name=first_name, last_name=last_name, username=username, user_category=user_category,
                                                        type_of_asset=type_of_asset, asset_name=asset_name,
                                                        vendor_name=vendor_name,
                                                        invoice_value=invoice_value, loan_amount=loan_amount, package_list=package_list)
        #stallion_smart_details = LoanPackages.objects.create(type_of_asset=type_of_asset,asset_name=asset_name, vendor_name=vendor_name,invoice_value=invoice_value,loan_amount=loan_amount, user=user)
        salary_earners_info.save();
        #stallion_smart_details.save();
        print('Loan Application Successful')
        return redirect('stallion_smart_loan')
    return render(request, 'loan/stallion_smart_form.html')


#approval part starts here

@login_required
def admin_approval(request):
    if request.method == 'POST':
        loan_approval = request.POST.get('action')
        admin_decision = Categories.objects.create(loan_approval=loan_approval)
        if loan_approval == 'AP':
            admin_decision.save(commit=True)
            return render(request,'loan/data-status=pending.html')
        elif loan_approval == 'DE':
            admin_decision.save(commit=False)
            return render(request, 'loan/data-status=pending.html')
        else:
            pass

        return redirect(loan_pending)

    return render(request, 'loan/data-status=pending.html')