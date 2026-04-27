from django.shortcuts import render
from core.models import Profile
from .models import Certificate
from .models import Project


def home(request):

    profile = Profile.objects.first() 
    certificates = Certificate.objects.all() 
    
    context = {
        'profile': profile,
        'certificates': certificates
    }

    return render(request, 'portfolio/home.html', context)

def projects(request):
    projects = Project.objects.all()
    
    context = {
        'projects': projects
    }

    return render(request, 'portfolio/projects.html', context)

def contacts(request):
    return render(request, 'portfolio/contacts.html')