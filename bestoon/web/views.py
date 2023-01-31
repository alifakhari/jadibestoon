from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from web.models import Token,Expense,Income,User
from django.views.decorators.csrf import csrf_exempt
from json import JSONEncoder
from datetime import datetime

csrf_exempt
def submit_expense(request):
    return HttpResponse("hi")

def blank_response(request):
    # Expense.objects.create(user="1", text="Parking", date = datetime.now(),amount="20000")
    
    return JsonResponse({
    "status": "OK!",
    # "Expense" : Expense.objects.filter(user=1)
    })
    # return HttpResponse('you are looking at my blank page')