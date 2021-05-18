from django.shortcuts import render
from django import forms
from django.urls import reverse
from .models import todolist

# Create your views here.

k=0
def index(request):
    global k
    if request.method == "POST":
        task=request.POST["new_task"]
        try:
            todolist.objects.get(task_info=task)
        except:
            if (task!=""):
                k+=1
                x=todolist(task_info=task, status=False, task_number=k)
                x.save()
    return render(request,"tasks/index.html", {
            "data": todolist.objects.all(),"update": True
        })

def done(request):
    action=request.POST["action"]
    if request.POST["action"] is False:
        return render(request,"tasks/index.html", {
            "data": todolist.objects.all(),"update": True
    })

    return render(request,"tasks/index.html", {
            "data": todolist.objects.all(),action: True
    })

def completed(request):
    if request.method == "POST":
        task=request.POST["completed"]
        todolist.objects.filter(task_number=task).update(status=True)
    return render(request,"tasks/index.html", {
            "data": todolist.objects.all(),"update": True
        })

def incomplete(request):
    if request.method == "POST":
        task=request.POST["incomplete"]
        todolist.objects.filter(task_number=task).update(status=False)
    return render(request,"tasks/index.html", {
            "data": todolist.objects.all(),"update": True
        })

def clear(request):
    if request.method == "POST":
        task=request.POST["clear"]
        todolist.objects.filter(task_number=task).delete()
    return render(request,"tasks/index.html", {
            "data": todolist.objects.all(),"update": True
        })
    
def clearall(request):
    todolist.objects.all().delete()
    return render(request,"tasks/index.html", {
            "data": todolist.objects.all()
        })
        