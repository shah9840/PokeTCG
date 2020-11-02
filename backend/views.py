from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import objects
import json
# Create your views here.

def homepage(request):
    pokelist,pokelist_json=objects.getobjects()
    return render(request,
                  'backend/index.html', {'list_json':json.dumps(pokelist_json),
                                         'list':pokelist})

def login(request):
    return render(request = request,
                  template_name = "backend/login.html")
