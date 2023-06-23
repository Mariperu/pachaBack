from django.shortcuts import render
from culqi import __version__
from culqi.client import Culqi
from culqi.resources import Card
from culqi.resources import Customer
from culqi.resources import Charge
import json
from django.http import HttpResponse


public_key = "pk_test_89a1417406ce7fa2"
private_key = "sk_test_SWyklAB8rIyjXmje"

def Home(request): # Primera Funcion Vista Home
    return render(request, 'cliente/index.html') #retorna la vista


def generateCharge(request):
    body = request.json
    version = __version__

    culqi = Culqi(public_key, private_key)
    charge = Charge(client=culqi)
    card = charge.create(body)
    print(card)
    return HttpResponse(json.dumps(card["data"]), content_type="application/json")