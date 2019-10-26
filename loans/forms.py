from django.forms import ModelForm
from .models import Document

class BankStatementForm(ModelForm):

    class Meta:
        model = Document
        fields = ('bank_statement',)
