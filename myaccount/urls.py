from django.urls import path
from . import views

app_name = 'myaccount'

urlpatterns = [
    path('', views.AccountMessageCreateView.as_view(), name = 'myaccount'),

]