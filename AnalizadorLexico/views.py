from django.shortcuts import render
from django.http import JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from .src.lexema import Data
import json

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def resulHome(request):
    if request.method == 'POST':
        myVar = json.loads(request.body)
        return JsonResponse({"data" : Data(myVar['data'])})
    return JsonResponse()