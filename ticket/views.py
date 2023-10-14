from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import TicketCreateForm








class TicketCreateView(LoginRequiredMixin, CreateView):
    form_class = TicketCreateForm
    template_name = 'ticket.html'
    success_url = reverse_lazy(('user:success'))

    def form_valid(self, form):
        ticket = form.save(commit=False)
        ticket.created_by = self.request.user 
        ticket.save()
        return super().form_valid(form)
    

