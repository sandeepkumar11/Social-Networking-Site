from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


class UserCreateForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'placeholder':'Password','class':'form-control'}
    ))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={'placeholder':'Confirm Password','class':'form-control'}
    ))

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'placeholder':'Email ID','class':'form-control'}
    ))
    class Meta:
        model = User
        fields = ('username','email')
        widgets = {'username':forms.TextInput(
            attrs={'placeholder':'Username','class':'form-control'}
        )}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'placeholder':'Username','autofocus':True,
        'class':'form-control',}
    ))
    password = forms.CharField(
        label = "Password",
        strip = False,
        widget = forms.PasswordInput(
            attrs={'placeholder':'Password','autocomplete':'current-password',
            'class':'form-control'}
        ),
    )
