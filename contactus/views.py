from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ContactUsCreateForm
from .models import ContactInfo








class ContactUsCreateView(CreateView):
    form_class = ContactUsCreateForm
    template_name = 'contact-us.html'
    success_url = reverse_lazy('user:success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact_info = ContactInfo.objects.all()
        if contact_info.count() != 0:
            context['contact_info'] = contact_info[0]
        return context

    

