from .views import RegisterView, home_view, ProfileView, PostListView
from django.contrib.auth import views as auth_view
from django.urls import path

urlpatterns = [
        path("", home_view, name="home"),
        path("profile/", ProfileView.as_view, name="profile"),
        path("register/", RegisterView.as_view(), name="register"),
        path("login/", auth_view.LoginView.as_view(template_name="blog/login.html"), name="login"),
        path("logout/", auth_view.LogoutView.as_view(), name="logout"),
        path('posts/', PostListView.as_view(), name='posts'),
        ]
