from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bosh_sahifa(request):
    return HttpResponse("<html><title>To-Do lists</title><body><h1>To-Do lists</h1></body></html>")