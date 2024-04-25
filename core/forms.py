from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')
    username=forms.CharField(widget=forms.TextInput(attrs={
                            'placeholder':'Your Username',
                            'class':'w-full rounded-xl px-6 py-3'
                            }))
    email=forms.CharField(widget=forms.EmailInput(attrs={
                            'placeholder':'Your email address',
                            'class':'w-full rounded-xl px-6 py-3'
                            }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
                            'placeholder':'Password',
                            'class':'w-full rounded-xl px-6 py-3'
                            }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
                            'placeholder':'Repeat Password',
                            'class':'w-full rounded-xl px-6 py-3'
                            }))
class loginform(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
                            'placeholder':'Your Username',
                            'class':'w-full rounded-xl px-6 py-3'
                            }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
                            'placeholder':'Password',
                            'class':'w-full rounded-xl px-6 py-3'
                            }))
