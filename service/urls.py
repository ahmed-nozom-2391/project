from django.urls import path
from . import views
from .models import Service

app_name = 'service'

urlpatterns = [
    path('', views.Service.as_view(), name = 'all_service'),
    path('<str:slug>', views.ServiceDetailView.as_view(model=Service), name = 'service'),

]