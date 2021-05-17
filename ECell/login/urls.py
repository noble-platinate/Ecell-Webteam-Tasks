from django.urls import path

from . import views

app_name = "login"

urlpatterns = [
    path("login",views.index,name="index"),
    path("register",views.register,name="register")
]