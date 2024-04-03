from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index (request):
    return HttpResponse('Hello World. This is the index page')
def new(request):
    return HttpResponse('New products')