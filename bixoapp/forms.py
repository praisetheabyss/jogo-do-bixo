from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    username = forms.CharField(required=False)
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