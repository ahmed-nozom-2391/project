from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token
from .utils import get_username, expired
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import SignUpForm
from project.settings import TARGET_DATE
from django.urls import reverse_lazy




def index(request):
    if expired(TARGET_DATE):
        return
    return render(request, "index.html")



@requires_csrf_token
@csrf_exempt
@csrf_protect
def login_view(request):
    context = {'error':''}

    if request.user.is_authenticated: 
        return redirect("user:index")
    
    
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        
        username = get_username(username)
        
        user = authenticate(username=username, password=password)
        if user :
            login(request, user)
            return redirect("user:index")
        else :
            # add google login note
            context['error'] = "Invalid Login" 
    return render(request, 'login.html' , context)



class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'sign-up.html'
    success_url = reverse_lazy('user:success_sign')

def success_sign(request):
    return render(request, "success_sign.html")

    
def logout_view(request):
    logout(request)
    return redirect('user:index')



@login_required
def success_send(request):
    return render(request, "success.html")






from myaccount.models import MyService
from service.models import Service

def base_context(request):
    user = request.user
    cart_services = 0
    if user.is_authenticated:
        services = MyService.objects.filter(user = user)
        cart_services = services.count()

    service_list = Service.objects.all()

    return {
            'cart_services': cart_services,
            'service_list' : service_list
            }
    