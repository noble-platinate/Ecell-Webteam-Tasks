from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "gallary/index.html")

def gal(request,name):
    messi=ronaldo=lewan=False
    if name == 1: 
        messi=True
        return render(request, "gallary/gallary.html", {
        "messi": messi, "ronaldo":ronaldo, "lewan":lewan
    })
    elif name == 2: 
        ronaldo=True
        return render(request, "gallary/gallary.html", {
        "messi": messi, "ronaldo":ronaldo, "lewan":lewan
    })
    elif name == 3:
        lewan=True
        return render(request, "gallary/gallary.html", {
        "messi": messi, "ronaldo":ronaldo, "lewan":lewan
    })
    return render(request, "gallary/index.html")