from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView
)
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post
from .forms import CustomUserCreationForm


# ---------- HOME VIEW ----------
def home_view(request):
    return render(request, 'blog/home.html')


# ---------- USER REGISTRATION ----------
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


# ---------- USER PROFILE ----------
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

        # Update fields only if provided
        if username:
            user.username = username
        if email:
            user.email = email

        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')


# ---------- BLOG POST CRUD VIEWS ----------

# List all posts (READ - list)
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


# View single post (READ - detail)
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


# Create a new post (CREATE)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update a post (UPDATE)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Allow only post author to update"""
        post = self.get_object()
        return self.request.user == post.author


# Delete a post (DELETE)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        """Allow only post author to delete"""
        post = self.get_object()
        return self.request.user == post.author
