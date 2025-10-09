from django.shortcuts import render,
redirect
from django.views import view
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationFormfrom django.contrib import messages
from django.contrib.auth.models import User
from django.utils.decorators import metho
d_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request):
    return render(request, 'blog/home.html')

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

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    template_name = 'blog/profile.html'

    def get(self, request):
        """Display user profile details"""
        return render(request, self.template_name, {'user': request.user})

    def post(self, request):
        """Handle profile updates"""
        user = request.user
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Update the fields if they were provided
        if username:
            user.username = username
        if email:
            user.email = email

        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
