from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Service
from myaccount.models import MyService



class Service(ListView):
    queryset      = Service.objects.all()
    template_name = "service.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_object_list = context['object_list']
        nol = self.get_triple(new_object_list)
        triple_list = list(zip(nol, range(len(nol))))
        context['new_object_list'] = triple_list

        if self.request.user.is_authenticated:
            my_cart     = MyService.objects.filter(user = self.request.user)
            my_services = [i.service for i in my_cart]
            context['my_services'] = my_services
        return context
    
    def get_triple(self, x):
        c = [[] for i in range(0,len(x),3)]
        for i,v in enumerate(range(0,len(x), 3)):
            c[i].append(x[v])
            if v+1 < len(x):
                c[i].append(x[v+1])
            if v+2 < len(x):
                c[i].append(x[v+2])
        return c




class ServiceDetailView(DetailView):
    template_name = 'service_detail.html'