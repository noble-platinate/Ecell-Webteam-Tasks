from django.urls import path

from . import views

app_name = "linkedin"

urlpatterns = [
    path("",views.index,name="index"),
]