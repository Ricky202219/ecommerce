from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegistroForm(UserCreationForm):
    nombre_completo = forms.CharField(max_length=50, label='Nombre Completo', widget=forms.TextInput(attrs={'class': 'ps-2 form-control mb-3 border-black'}))
    correo_electronico = forms.EmailField(label='Correo Electrónico', widget=forms.EmailInput(attrs={'class': 'ps-2 form-control mb-3 border-black'}))
    direccion_envio = forms.CharField(max_length=200, label='Dirección de Envío', widget=forms.TextInput(attrs={'class': 'ps-2 form-control mb-3 border-black'}))
    telefono_contacto = forms.CharField(max_length=20, label='Teléfono de Contacto', widget=forms.TextInput(attrs={'class': 'ps-2 form-control mb-3 border-black'}))
    region = forms.CharField(max_length=20, label='Región', widget=forms.TextInput(attrs={'class': 'ps-2 form-control mb-3 border-black'}))
    ciudad = forms.CharField(max_length=20, label='Ciudad', widget=forms.TextInput(attrs={'class': 'ps-2 form-control mb-3 border-black'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'nombre_completo', 'correo_electronico', 'direccion_envio', 'telefono_contacto','region','ciudad', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'ps-2 form-control mb-3 border-black'}),
            'password1': forms.PasswordInput(attrs={'class': 'ps-2 form-control mb-3 border-black'}),
            'password2': forms.PasswordInput(attrs={'class': 'ps-2 form-control mb-3 border-black'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'ps-2 form-control mb-3 border-black'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'ps-2 form-control mb-3 border-black'}))
