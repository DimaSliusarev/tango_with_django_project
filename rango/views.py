from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    contest_dict = {'boldmessage' : 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render (request, 'rango/index.html', context = contest_dict)

def about (request):
    return render (request, 'rango/about.html')