from django.shortcuts import render, redirect,HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

class LoginView(View):
    def get(self,request):
        fm = forms.LoginForm()
        return render(request,'accounts/login.html',{'form':fm})

    def post(self,request):
        fm = forms.LoginForm(request, data=request.POST)

        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']

            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request, 'Logged in Successfully!!')
                return HttpResponseRedirect('/')
            else:
                # messages.error(request,'username or password not correct')
                return redirect('accounts/login.html')
        else:
            messages.error(request,'username or password is not correct')
            return render(request,'accounts/login.html',{'form':fm})

