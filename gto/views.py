from django.shortcuts import render
from .models import Standard, Document, News, Partner

def index(request):
    return render(request, "gto/index.html")

def standards(request):
    standards = Standard.objects.all()
    return render(request, "gto/standards.html", {"standards": standards})

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return render(request, "gto/signup.html", {
            "success": True,
            "name": name,
            "age": age
        })

    return render(request, "gto/signup.html")

def documents(request):
    docs = Document.objects.all().order_by("-published_at")
    return render(request, "gto/documents.html", {"docs": docs})

def news(request):
    news = News.objects.all().order_by("-published_at")
    return render(request, "gto/news.html", {"news": news})

def partners(request):
    partners = Partner.objects.all()
    return render(request, "gto/partners.html", {"partners": partners})
