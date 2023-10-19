from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import AccountMessageCreateForm
from .models import MyService







class AccountMessageCreateView(LoginRequiredMixin, CreateView):
    form_class = AccountMessageCreateForm
    template_name = 'my-account.html'
    success_url = reverse_lazy('user:success')

    def form_valid(self, form):
        message = form.save(commit=False)
        message.created_by = self.request.user 
        message.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        services = MyService.objects.filter(user = user)
        context['services'] = services
        return context
    

    



    

