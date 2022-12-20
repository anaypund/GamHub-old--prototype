from django.shortcuts import render

def index(request):
    return render(request, "soul/index.html")

def homepage(request):
    return render(request, "soul/page.html")

def contactUs(request):
    return render(request, "soul/contact.html")

def basic(request):
    return render(request, "soul/basic.html")

def faq(request):
    return render(request, "soul/faq.html")

def watching(request):
    return render(request, "soul/watching.html")

def social(request):
    return render(request, "soul/social.html")

def matched(request):
    return render(request, "soul/matched.html")

def registered(request):
    username=request.POST("email")
    password=request.POST("pass")
    print(username, password)