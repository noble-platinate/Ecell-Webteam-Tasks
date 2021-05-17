from django.shortcuts import render
from .models import user_data

# Create your views here.

def index(request="GET"):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        try:
            x=user_data.objects.get(username=username)
            try:
                x=user_data.objects.get(username=username, password=password)
                return render(request, "login/user.html",{
                    "data":x
                })
            except:
                return render(request, "login/index.html", {
                    "message": "Invalid login credentials"
                })
        except:
            return render(request, "login/index.html", {
                "message": "User does not exist, please register!"
            })
    return render(request, "login/index.html")

def register(request="GET"):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        username=request.POST["username"]
        password=request.POST["password"]
        email=request.POST["email"]
        try:
            x=user_data.objects.get(username=username)
            return render(request, "login/register.html", {
                "message": "Username already used!"
            })
        except:
            x=user_data(fname=fname, lname=lname, username=username, password=password,email=email)
            x.save()
            return render(request, "login/index.html")
    return render(request, "login/register.html")