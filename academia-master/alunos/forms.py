from django import forms
from django.contrib.auth.models import User
from .models import Aluno_Usuario


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = Aluno_Usuario
        fields = ('email', 'password', 'nome', 'sobrenome','cpf','data_de_nascimento','endereço','telefone','sexo','altura','peso_inicial',
                  'peso_atual','peso_objetivo','is_staff')

