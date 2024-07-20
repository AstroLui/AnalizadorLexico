from django.shortcuts import render
from django.http import JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from .src.lexema import Data
from .src.jejeje import Run, getArrayErrors
from .src.traductor import js_to_py
from .src.prueba import sintactico
from .src.tr2 import translate_js_to_py
import json

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def resulHome(request):
    if request.method == 'POST':
        myVar = json.loads(request.body)
        sintactic_result = sintactico(myVar['data'])
        return JsonResponse({"data" : Data(myVar['data']),
                             "sint" : sintactic_result,
                             "err" : getArrayErrors(), 
                             "trad" : translate_js_to_py(myVar['data'])})
    return JsonResponse()