from django.shortcuts import render
from django.http import JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from .src.lexema import Data
from .src.jejeje import Run, getArrayErrors
from .src.traductor import js_to_py
import json

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def resulHome(request):
    if request.method == 'POST':
        myVar = json.loads(request.body)
        return JsonResponse({"data" : Data(myVar['data']),
                             "sint" : Run(myVar['data']),
                             "err" : getArrayErrors(), 
                             "trad" : js_to_py(myVar['data'])})
    return JsonResponse()