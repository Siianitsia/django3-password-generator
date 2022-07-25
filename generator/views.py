from django.shortcuts import render
import random
from string import ascii_lowercase, ascii_uppercase, digits


def home(request): #home page
    return render(request, 'generator/home.html')


def password(request): #password generation

    characters = list(ascii_lowercase)
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):   #add uppercase
        characters.extend(list(ascii_uppercase))

    if request.GET.get('numbers'):   #add numbers
        characters.extend(list(digits))

    if request.GET.get('special'):   #add special chars
        characters.extend(list('!@#$%^&*()/|_'))

    thepassword = ''
    for _ in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def info(request):
    return render(request, 'generator/info.html')
