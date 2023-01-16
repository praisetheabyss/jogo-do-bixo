from random import choice
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from bixoapp.forms import CustomUserForm, CustomAutheticationForm, SorteioForm, ApostasGrupoForm, ApostasDuqueForm, ApostasTernoForm, ApostasQuadraForm, ApostasQuinaForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views
from bixoapp.models import *
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

hoje = datetime.today()

dia = hoje.day
mes = hoje.month
ano = hoje.year

hora = datetime(ano, mes, dia, 12, 00, 00)

yesterday = timezone.now() - timezone.timedelta(days=1)



# Create your views here.

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

@staff_member_required
def sorteio(request):
    data = {}
    form = SorteioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    data['form'] = form
    return render(request, 'sorteio.html', data)

def home(request):
    pks = RandomFrases.objects.values_list('pk', flat=True)
    random_pk = choice(pks)

    random_obj = RandomFrases.objects.filter(pk=random_pk)

    bixo_list = Animais.objects.all()
    apostas_list = ApostasGrupo.objects.all()

    today = datetime.today()

    year = today.year
    month = today.month
    day = today.day

    sorteios_list = Sorteios.objects.filter(data_do_sorteio__year=year, data_do_sorteio__month=month, data_do_sorteio__day=day)


    return render(request, 'index.html', {'bixo_list':bixo_list,'sorteios_list':sorteios_list,'apostas_list':apostas_list, 'random_obj': random_obj})

@login_required
def apostasGrupo(request):
    if ApostasGrupo.objects.filter(user=request.user, data_da_aposta__gt=yesterday).exists():
        return render(request, 'error/numerodeapostas.html')
    if datetime.now() < hora:
        data = {}
        form = ApostasGrupoForm(request.POST or None)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')

        data['form'] = form
        return render(request, 'apostas/grupo.html', data)
    else:
        return render(request, 'error/tempodeapostas.html')
    

@login_required
def apostasDuque(request):
    if ApostasDuque.objects.filter(user=request.user, data_da_aposta__gt=yesterday).exists():
        return render(request, 'error/numerodeapostas.html')
    if datetime.now() < hora:
        data = {}
        form = ApostasDuqueForm(request.POST or None, initial={'primeiro_num_apostado': '1', 'segundo_num_apostado': '1'})

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
        else:
            print(form.errors)
            
        data['form'] = form
        return render(request, 'apostas/duque.html', data)
    else:
        return render(request, 'error/tempodeapostas.html')

@login_required
def apostasTerno(request):
    if ApostasTerno.objects.filter(user=request.user, data_da_aposta__gt=yesterday).exists():
        return render(request, 'error/numerodeapostas.html')
    if datetime.now() < hora:
        data = {}
        form = ApostasTernoForm(request.POST or None, initial={'primeiro_num_apostado': '1', 'segundo_num_apostado': '1', 'terceiro_num_apostado': '1'})

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
        else:
            print(form.errors)
            
        data['form'] = form
        return render(request, 'apostas/terno.html', data)
    else:
        return render(request, 'error/tempodeapostas.html')

@login_required
def apostasQuadra(request):
    if ApostasQuadra.objects.filter(user=request.user, data_da_aposta__gt=yesterday).exists():
        return render(request, 'error/numerodeapostas.html')
    if datetime.now() < hora:
        data = {}
        form = ApostasQuadraForm(request.POST or None, initial={'primeiro_num_apostado': '1', 'segundo_num_apostado': '1', 'terceiro_num_apostado': '1', 'quarto_num_apostado': '1'})

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
        else:
            print(form.errors)
            
        data['form'] = form
        return render(request, 'apostas/quadra.html', data)
    else:
        return render(request, 'error/tempodeapostas.html')

@login_required
def apostasQuina(request):
    if ApostasQuina.objects.filter(user=request.user, data_da_aposta__gt=yesterday).exists():
        return render(request, 'error/numerodeapostas.html')
    if datetime.now() < hora:
        data = {}
        form = ApostasQuinaForm(request.POST or None, initial={'primeiro_num_apostado': '1', 'segundo_num_apostado': '1', 'terceiro_num_apostado': '1', 'quarto_num_apostado': '1', 'quinto_num_apostado': '1'})

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
        else:
            print(form.errors)
            
        data['form'] = form
        return render(request, 'apostas/quina.html', data)
    else:
        return render(request, 'error/tempodeapostas.html')

def resultado(request):
    bixo_list = Animais.objects.all()

    today = datetime.today()

    year = today.year
    month = today.month
    day = today.day

    apostas_list = ApostasGrupo.objects.filter(data_da_aposta__year=year, data_da_aposta__month=month, data_da_aposta__day=day, user = request.user)
    apostas_duque_list = ApostasDuque.objects.filter(data_da_aposta__year=year, data_da_aposta__month=month, data_da_aposta__day=day, user = request.user)
    apostas_terno_list = ApostasTerno.objects.filter(data_da_aposta__year=year, data_da_aposta__month=month, data_da_aposta__day=day, user = request.user)
    apostas_quadra_list = ApostasQuadra.objects.filter(data_da_aposta__year=year, data_da_aposta__month=month, data_da_aposta__day=day, user = request.user)
    apostas_quina_list = ApostasQuina.objects.filter(data_da_aposta__year=year, data_da_aposta__month=month, data_da_aposta__day=day, user = request.user)


    sorteios_list = Sorteios.objects.filter(data_do_sorteio__year=year, data_do_sorteio__month=month, data_do_sorteio__day=day)

    

    return render(request, 'apostas/resultado.html', {'bixo_list':bixo_list,'sorteios_list':sorteios_list,'apostas_list':apostas_list, 'apostas_duque_list': apostas_duque_list, 'apostas_terno_list': apostas_terno_list, 'apostas_quadra_list': apostas_quadra_list, 'apostas_quina_list': apostas_quina_list,})