from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import AccountMessageCreateForm








class AccountMessageCreateView(LoginRequiredMixin, CreateView):
    form_class = AccountMessageCreateForm
    template_name = 'my-account.html'
    success_url = reverse_lazy('user:success')

    def form_valid(self, form):
        message = form.save(commit=False)
        message.created_by = self.request.user 
        message.save()
        return super().form_valid(form)
    

0

    

