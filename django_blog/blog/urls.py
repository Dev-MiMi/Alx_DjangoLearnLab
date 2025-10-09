from .views import (
    RegisterView,
    home_view,
    ProfileView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
from django.contrib.auth import views as auth_view
from django.urls import path

urlpatterns = [
    path("", home_view, name="home"),
    path("profile/", ProfileView.as_view, name="profile"),
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "login/",
        auth_view.LoginView.as_view(template_name="blog/login.html"),
        name="login",
    ),
    path("logout/", auth_view.LogoutView.as_view(), name="logout"),
    path("posts/", PostListView.as_view(), name="posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]
