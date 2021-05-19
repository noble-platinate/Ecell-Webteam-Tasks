from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = "gallary"

urlpatterns = [
    path("",views.index,name="index"),
    path("<int:name>",views.gal,name="gal")
]

urlpatterns += staticfiles_urlpatterns()
