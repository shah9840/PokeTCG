from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import objects
# Create your views here.

def homepage(request):
    pokelist=objects.getobjects()
    return render(request,
                  'backend/index.html', {'list':pokelist})

def login(request):
    return render(request = request,
                  template_name = "backend/login.html")
