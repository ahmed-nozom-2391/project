from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token
from .utils import get_username
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy


def index(request):
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
    success_url = reverse_lazy('user:login')



    
def logout_view(request):
    logout(request)
    return redirect('user:index')



@login_required
def success_send(request):
    return render(request, "success.html")



