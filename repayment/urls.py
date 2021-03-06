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

#repayment part starts here
    path('make-payment/<int:id>', views.make_payment, name = 'make_payment'),
    #path('create-payment/<int:id>', views.create_payment_process, name = 'create_payment_process'),
    path('data/', views.repayment, name = 'repayment'),
    path('client_data/<int:id>', views.client_repayment_history, name = 'client_repayment_history'),
    path('card-details/<int:id>', views.initiate_card_first_transaction, name ='initiate_card_first_transaction'),
    path('card-verified', views.verify_card_payment, name = 'verify_card_payment')
    ]