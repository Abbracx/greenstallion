"""greenstallion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [

    #borrower starts here
    path('loan-details/data/<int:id>', views.loan_detail, name = 'loan_detail'),
    path('user-bank-statement/<int:id>', views.user_bank_statement, name = 'user_bank_statement'),

    path('borrower/data-active=0', views.borrower_pending, name = 'borrower_pending'),
    path('borrower/create', views.borrower_create, name = 'borrower_create'),
    path('borrower/group/data', views.borrower_group_data, name = 'borrower_group_data'),
    path('borrower/group/create', views.borrower_group_create, name = 'borrower_group_create'),

    #loan starts here
    path('loan/apply_loan/<int:id>', views.apply_loan, name = 'apply_loan'),
    path('loan/income-details/<int:id>', views.process_eligible_loan, name = 'process_eligible_loan'),
    path('loan/data', views.loan_data, name = 'loan_data'),
    path('loan/data-status=pending/', views.loan_pending, name = 'loan_pending'),
    path('loan/data-status=approved/', views.loan_approved, name = 'loan_approved'),
    path('loan/data-status=declined/', views.loan_declined, name = 'loan_declined'),
    path('loan/data-status=withdrawn', views.loan_withdrawn, name = 'loan_withdrawn'),
    path('loan/data-status=written_off', views.loan_writtenoff, name = 'loan_writtenoff'),
    path('loan/data-status=closed/', views.loan_closed, name = 'loan_closed'),
    path('loan/data-status=loan_disbursed/', views.loan_disbursed, name = 'loan_disbursed'),
    path('loan/create', views.loan_create, name = 'loan_create'),
    path('loan/loan_application/data/', views.loan_applications, name = 'loan_applications'),
    path('loan/loan_product/data', views.loan_products, name = 'loan_products'),
    path('charge/data', views.loan_charges, name = 'loan_charges'),
    path('loan/loan_disbursed_by/data', views.loan_disbursedby, name = 'loan_disbursedby'),
    path('loan/loan_repayment_method/data', views.loan_repayment_method, name = 'loan_repayment_method'),
    path('loan/provision/data', views.loan_provision_rate, name = 'loan_provision_rate'),
    path('loan/loan_calculator/create', views.loan_calculator, name = 'loan_calculator'),
    path('guarantor/data', views.loan_guarantors, name = 'loan_guarantors'),


#the collateral part starts here
    path('collateral/data', views.view_collaterals, name = 'view_collaterals'),
    path('collateral/type/data', views.collateral_types, name = 'collateral_types'),

# stallion loan packages are here
    path('loan/stallion_smart_form/<int:id>', views.stallion_smart_loan, name = 'stallion_smart_loan'),
    path('loan/stallion_fees_form/<int:id>', views.stallion_fees_loan, name = 'stallion_fees_loan'),
    path('loan/stallion_allowee_form/<int:id>', views.stallion_allowee_loan, name = 'stallion_allowee_loan'),
    path('loan/stallion_support_form/<int:id>', views.stallion_support_loan, name = 'stallion_support_loan'),
    path('loan/stallion_advance_form/<int:id>', views.stallion_advance_loan, name = 'stallion_advance_loan'),
    path('loan/stallion_loans_form/<int:id>', views.stallion_loans_loan, name = 'stallion_loans_loan'),

    ]