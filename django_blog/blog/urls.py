from .views import RegisterView, home_view
from django.urls import path
from django.contrib.auth import views as auth_view

urlpatterns = [
        path("", home_view, name="home"),
        path("register/", RegisterView.as_view(), name="signup"),
        path("login/", auth_view.LoginView.as_view(), name="login"),
        path("logout/", auth_view.LogoutView.as_view(), name="logout"),
        ]
