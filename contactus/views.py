from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ContactUsCreateForm








class ContactUsCreateView(CreateView):
    form_class = ContactUsCreateForm
    template_name = 'contact-us.html'
    success_url = reverse_lazy('user:success')

    

