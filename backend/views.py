from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import objects
import json

# Create your views here.
def win(request):
    return render(request,'backend/win.html')

def lose(request):
    return render(request,'backend/lose.html')

def battle(request):
    try:
        user = request.session['user']
    except:
        user = None;

    if request.method == 'POST':
        egg = dict(request.POST)
        newPoke = egg.get('newPoke[]')
        byePoke = egg.get('byePoke[]')
        res = egg.get('result')
        print("Yahallo")
        objects.addCards(user,newPoke)
        objects.subCards(user,byePoke)

    if (user is not None):
        request.session.modified = True
        print(user)
        pokelist,pokelist_json=objects.getobjects(user)
        oppnentlist, opponentlist_json = objects.getobjects_of_opponent(user)
        return render(request,
                      'backend/index.html', {'list_json':json.dumps(pokelist_json),
                                             'list':pokelist,
                                             'opplist_json':json.dumps(opponentlist_json),
                                             'opplist':oppnentlist})
    else:
        return redirect('backend:login')

def login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pasw = request.POST.get('password')
        request.session['user'] = user
        if (objects.checkAcc(user,pasw)):
            return redirect('backend:battle')
        else:
            return redirect('backend:login')

    return render(request = request,
                  template_name = "backend/login.html")
