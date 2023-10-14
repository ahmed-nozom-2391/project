from django import forms
from .models import ContactUs



class ContactUsCreateForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name',
                  'email',
                  'message',
                   )




