from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import PortFolio



class PortFolio(ListView):
    queryset      = PortFolio.objects.all()
    template_name = "portfolio.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_object_list = context['object_list']
        nol = self.get_couple(new_object_list)
        coupled_list = list(zip(nol, range(len(nol))))
        context['new_object_list'] = coupled_list
        
        return context
    
    def get_couple(self, x):
        c = [[] for i in range(0,len(x),2)]
        for i,v in enumerate(range(0,len(x), 2)):
            c[i].append(x[v])
            if v+1 < len(x):
                c[i].append(x[v+1])
        return c



