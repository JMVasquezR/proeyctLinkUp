from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"type": "text", "name": "username", "id": "username", "class": "form-control"}), required=True)
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={"type": "password", "name": "password", "id": "password", "class": "form-control"}), required=True)
