from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login', views.login_view, name = 'login'),
    path('logout', views.logout_view, name = 'logout'),
    path('signup', views.SignUp.as_view(), name = 'signup'),
    path('success', views.success_send, name = 'success'),
    path('success_sign', views.success_sign, name = 'success_sign'),

]