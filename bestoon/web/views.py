from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def submit_expense(request):
    return HttpResponse("hi")

def blank_response(request):
    return HttpResponse('you are looking at my blank page')