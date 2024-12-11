from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import PasswordResetView
from django.views import View
from .forms import RegistrationForm

class UserRegistrationView(View):
    form_class = RegistrationForm
    template_name = 'registration/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password2')
            account = authenticate(username=username, password=password)
            login(request, account)
            return redirect('home')
        return render(request, self.template_name, {'form': form})
        
