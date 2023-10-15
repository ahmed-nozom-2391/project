from django.urls import path
from . import views, api

app_name = 'myaccount'

urlpatterns = [
    path('', views.AccountMessageCreateView.as_view(), name = 'myaccount'),
    path('my-cart', api.CartApi.as_view(), name = 'mycart'),

]