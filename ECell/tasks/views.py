from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
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
            "data": todolist.objects.all()
        })

def done(request):
    task=request.POST["done_task"]
    todolist.objects.filter(task_number=task).update(status=True)
    return render(request,"tasks/index.html", {
            "data": todolist.objects.all()
        })

def clearall(request):
    todolist.objects.all().delete()
    return render(request,"tasks/index.html", {
            "data": todolist.objects.all()
        })