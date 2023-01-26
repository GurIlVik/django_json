from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

import random
import json


def times ():
    datetime_obj = datetime.now()
    datetime_str = datetime_obj.strftime("%d%b%Y%H%M%S")
    print(datetime_obj)
    return datetime_str

def create_example():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return str(a) + " + " + str(b), a + b
    

def index(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        print(body_data)
        # a_value = 996677
        return HttpResponse(json.dumps(
            {'a_field': times ()}
        ))
    context = {
        "examples_math": [
            create_example(),
            create_example(),
            create_example()
        ],
        "i_am_teacher": True   
    }
    return render(
        request,               # Запрос
	    'fenster/index.html',  # путь к шаблону
        context                # подстановки
    )
