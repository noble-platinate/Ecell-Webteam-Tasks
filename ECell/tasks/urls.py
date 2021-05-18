from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("",views.index,name="index"),
    path("done",views.done,name="done"),
    path("clearall",views.clearall,name="clearall"),
    path("clear",views.clear,name="clear"),
    path("completed",views.completed,name="completed"),
    path("incomplete",views.incomplete,name="incomplete")
]