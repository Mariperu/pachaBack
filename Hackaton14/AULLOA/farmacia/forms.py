from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username  = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class" : "text-xl p-2 rounded-xl bg-[#262B37] border-none outline-none"
            }
        )
    )
    
    password  = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "class" : "text-xl p-2 rounded-xl bg-[#262B37] border-none outline-none"
            }
        )
    )

class SignUpform(UserCreationForm):
    username  = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class" : "text-xl p-2 rounded-xl bg-[#262B37] border-none outline-none"
            }
        )
    )
    email  = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class" : "text-xl p-2 rounded-xl bg-[#262B37] border-none outline-none"
            }
        )
    )
    password1  = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "class" : "text-xl p-2 rounded-xl bg-[#262B37] border-none outline-none"
            }
        )
    )
    password2  = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "class" : "text-xl p-2 rounded-xl bg-[#262B37] border-none outline-none"
            }
        )
    )

    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2', 'is_admin', 'is_seller'}
