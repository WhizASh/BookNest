from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

class Loginform(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'Your Username',
            #class that fomr inpur filed for django
            'class' : "w-full rounded-xl px-6 py-6"
        }), max_length=20, required=False)
    
    password = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'Your password',
            'class' : "w-full rounded-xl px-6 py-6"
        }))
    


class SignUpform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'Your Username',
            'class' : "w-full rounded-xl px-6 py-6"
        }), max_length=20, required=False)
    
    email = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'Your Email',
            'class' : "w-full rounded-xl px-6 py-6"
        }))
    
    password1 = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'Your password',
            'class' : "w-full rounded-xl px-6 py-6"
        }))
    
    password2 = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'Your Repeat password',
            'class' : "w-full rounded-xl px-6 py-6"
        }))