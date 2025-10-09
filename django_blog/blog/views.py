from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

# Create your views here.

def home_view(request):
    return render(request, 'blog/home.html')

# blog/views.py
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messagesi
from .forms import CustomUserCreationForm

class RegisterView(View):
    template_name = 'blog/register.html'

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account was created successfully!")
            return redirect('login')
        return render(request, self.template_name, {'form': form})

