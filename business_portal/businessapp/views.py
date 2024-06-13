from django.shortcuts import render
from .models import Navbar
# Create your views here.

def home(request):
    views = {}
    views["navbar"]= Navbar.objects.all()
    return render(request, 'index.html')