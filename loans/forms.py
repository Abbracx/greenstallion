from django.forms import ModelForm
from .models import LoanAccount

class BankStatementForm(ModelForm):

    class Meta:
        model = LoanAccount
        fields = ('bank_statement',)
