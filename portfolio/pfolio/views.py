from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    return render(request, 'pfolio/index.html', {})

def about(request):
    return render(request, 'pfolio/about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def portfolio(request):
    return render(request, 'portfolio.html', {})

def skills(request):
    return render(request, 'skills.html', {})
