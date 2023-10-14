from django import forms
from .models import AccountMessage



class AccountMessageCreateForm(forms.ModelForm):
    class Meta:
        model = AccountMessage
        fields = ('message', )




