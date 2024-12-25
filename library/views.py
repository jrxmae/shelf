from django.shortcuts import render
from fjango.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the library!")