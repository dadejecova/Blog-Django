from django.http import HttpResponse ### delete this line
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
