from django.shortcuts import render
from .models import Subject

def home(request):
    return render(request, "core/home.html")

def subjects(request):
    subjects = Subject.objects.all()
    return render(request, "core/subjects.html", {"subjects": subjects})