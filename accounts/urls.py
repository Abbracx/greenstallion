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

#app_name = "accounts"
urlpatterns = [

    path('register/', views.register, name = 'register'),
    path('dashboard', views.dashboard, name ='dashboard'),
    path('', views.login, name = 'login'),
    path('logout', views.logout, name='logout'),
    path('user/profile', views.profile, name = 'profile'),

#reports part starts here
    path('report/borrower_report', views.report_borrower, name = 'report_borrower'),
    path('report/loan_report', views.report_loan, name = 'report_loan'),
    path('report/company_report', views.report_company, name ='report_company'),

#users part starts here
    path('user/data', views.view_users, name = 'view_users'),
    path('user/role/data', views.manage_user_roles, name = 'manage_user_roles'),
    path('user/create', views.user_creation, name = 'user_creation'),

#this is the settings part
    path('setting/data', views.settings, name = 'settings'),


    ]