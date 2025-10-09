from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Post

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

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

# Create a new post (CREATE)
class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")

# Update an existing post (UPDATE)
class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")

# Delete a post (DELETE)
class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")
