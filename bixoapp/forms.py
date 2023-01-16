from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from bixoapp.models import *
from django.core.exceptions import ValidationError

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username','email', 'first_name', 'last_name', 'password1', 'password2')

        def save(self, commit=True):
            user = super(CustomUserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user

class CustomAutheticationForm(AuthenticationForm):
    fields = ('email', 'password')

    email = forms.FileField(label='E-mail')
    class Meta:
        model = AuthenticationForm
        labels = {
            "username": "Email"
        }

class SorteioForm(ModelForm):
    class Meta:
        model = Sorteios
        fields = ['sorteio_do_dia','bixo_sorteado']

class ApostasGrupoForm(ModelForm):
    class Meta:
        model = ApostasGrupo
        fields = ('bixo_apostado', 'valor_apostado')

class ApostasDuqueForm(ModelForm):
    class Meta:
        model = ApostasDuque
        fields = ('primeiro_num_apostado', 'segundo_num_apostado', 'valor_apostado')
    
    def clean(self):
        primeiro = self.cleaned_data.get('primeiro_num_apostado')
        segundo = self.cleaned_data.get('segundo_num_apostado')
        if primeiro == segundo:
            raise forms.ValidationError("Os animais apostados precisam ser diferentes")
    

class ApostasTernoForm(ModelForm):
    class Meta:
        model = ApostasTerno
        fields = ('primeiro_num_apostado', 'segundo_num_apostado', 'terceiro_num_apostado', 'valor_apostado')

    def clean(self):
        primeiro = self.cleaned_data.get('primeiro_num_apostado')
        segundo = self.cleaned_data.get('segundo_num_apostado')
        terceiro = self.cleaned_data.get('terceiro_num_apostado')
        if primeiro == segundo or primeiro == terceiro or segundo == terceiro:
            raise forms.ValidationError("Os animais apostados precisam ser diferentes")

class ApostasQuadraForm(ModelForm):
    class Meta:
        model = ApostasQuadra
        fields = ('primeiro_num_apostado', 'segundo_num_apostado', 'terceiro_num_apostado', 'quarto_num_apostado', 'valor_apostado')

    def clean(self):
        primeiro = self.cleaned_data.get('primeiro_num_apostado')
        segundo = self.cleaned_data.get('segundo_num_apostado')
        terceiro = self.cleaned_data.get('terceiro_num_apostado')
        quarto = self.cleaned_data.get('quarto_num_apostado')
        if primeiro == segundo or primeiro == terceiro or primeiro == quarto or segundo == terceiro or segundo == quarto or terceiro == quarto:
            raise forms.ValidationError("Os animais apostados precisam ser diferentes")

class ApostasQuinaForm(ModelForm):
    class Meta:
        model = ApostasQuina
        fields = ('primeiro_num_apostado', 'segundo_num_apostado', 'terceiro_num_apostado', 'quarto_num_apostado', 'quinto_num_apostado', 'valor_apostado')

    def clean(self):
        primeiro = self.cleaned_data.get('primeiro_num_apostado')
        segundo = self.cleaned_data.get('segundo_num_apostado')
        terceiro = self.cleaned_data.get('terceiro_num_apostado')
        quarto = self.cleaned_data.get('quarto_num_apostado')
        quinto = self.cleaned_data.get('quinto_num_apostado')
        if primeiro == segundo or primeiro == terceiro or primeiro == quarto or primeiro == quinto or segundo == terceiro or segundo == quarto or segundo == quinto or terceiro == quarto or terceiro == quinto or quarto == quinto:
            raise forms.ValidationError("Os animais apostados precisam ser diferentes")
        
