from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "gallery/index.html")

def gal(request,name):
    messi=ronaldo=lewan=False
    if name == 1: 
        messi=True
        return render(request, "gallery/gallery.html", {
        "messi": messi, "ronaldo":ronaldo, "lewan":lewan, "name":name
    })
    elif name == 2: 
        ronaldo=True
        return render(request, "gallery/gallery.html", {
        "messi": messi, "ronaldo":ronaldo, "lewan":lewan, "name":name
    })
    elif name == 3:
        lewan=True
        return render(request, "gallery/gallery.html", {
        "messi": messi, "ronaldo":ronaldo, "lewan":lewan, "name":name
    })
    return render(request, "gallery/index.html")