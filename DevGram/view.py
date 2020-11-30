#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime

#from django.http.response import JsonResponse
import json


def hello_world(request):
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
    return HttpResponse(f'Oh hi, Current server time is {now}')

def sort_integers(request):
    """Return a JSON response with sorted integers."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )

def age_user(request, name, age):
    if age < 12:
        message = f'Sorry {name}, you are not allowed here'
    else:
        message = f'Hello {name}, Welcome to Platzigram'

    return HttpResponse(message)