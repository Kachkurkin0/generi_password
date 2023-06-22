from django.shortcuts import render
from django.http import  HttpResponse
import  random
# Create your views here.
def home(request):
    return render(request, 'generete/home.html')

def password(request):

    thepassword = ''
    characters = ['abcdefghigklmnopqrstuvwxyz']

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDIFGHIGKLMNOPRSTUVWXYZ'))

    elif request.GET.get('special'):
        characters.extend(list('~`!@#$%^&*()_+><?\|/;:'"<>.,"))

    elif request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    linght = int(request.GET.get('lenght'))

    for i in range(linght):
        thepassword += random.choice(characters)


    return render(request,'generete/password.html/', {'passwords':thepassword})

def creator(reqest):
    return render(reqest, 'generete/creator.html')

