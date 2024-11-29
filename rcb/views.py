from django.shortcuts import render
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h1> yuvraj is captain of csk</h1>')
def vicecaptain(request):
    return HttpResponse('<h1> jadeja is captain of csk</h1>')
# Create your views here.
