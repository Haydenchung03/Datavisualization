from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    return HttpResponse("<h1>Hello<h1>")

def v1(request):
    return HttpResponse("<h1>views 1<h1>")