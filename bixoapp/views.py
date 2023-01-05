from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from bixoapp.forms import CustomUserForm, CustomAutheticationForm, SorteioForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views
from bixoapp.models import *


# Create your views here.
def home(request):
    return render(request, 'index.html')

class SignUpView(generic.CreateView):
    form_class = CustomUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class LoginView(auth_views.LoginView):
    form_class = CustomAutheticationForm
    template_name = 'registration/login.html'

def logout_request(request):
	logout(request)
	return redirect("home")

def sorteio(request):
    return render(request, 'sorteio.html')

def sorteio(request):
    data = {}
    form = SorteioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    data['form'] = form
    return render(request, 'sorteio.html', data)