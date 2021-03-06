from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutPage, name="logout"),
]