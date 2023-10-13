from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token
from .utils import get_username
from django.contrib.auth import login, logout, authenticate
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

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        print('kwargs : ')
        print(kwargs)
        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
        return super().get_context_data(**kwargs)
    



    
def logout_view(request):
    logout(request)
    return redirect('user:index')