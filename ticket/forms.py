from django import forms
from .models import Ticket



class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('company_name',
                  'work_field',
                  'problem_type',
                  'suitable_time', 
                  'message',
                   )




