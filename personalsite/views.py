from django.shortcuts import render

def index(request):
    return render(request, 'personalsite/index.html')

def projects(request):
    return render(request, 'personalsite/projects.html')

def research(request):
    return render(request, 'personalsite/research.html')

def blog(request):
    return render(request, 'personalsite/blog.html')

def contact(request):
    return render(request, 'personalsite/contact.html')
