from django.urls import path

from . import views

app_name = "gallary"

urlpatterns = [
    path("",views.index,name="index"),
]