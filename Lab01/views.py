from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# ex: localhost:8080/app/
def index(request):
    return HttpResponse("Laboratorio 01!")

# ex: localhost:8080/app/sumar/num1/num2/
def suma(request,num1, num2):
    val1 = int(num1)
    val2 = int(num2)
    result = "El resultado de la suma: %s" % (val1+val2)
    return HttpResponse(result)

# ex: localhost:8080/app/restar/num1/num2/
def resta(request,num1, num2):
    val1 = int(num1)
    val2 = int(num2)
    result = "El resultado de la resta: %s" % (val1-val2)
    return HttpResponse(result)

# ex: localhost:8080/app/multiplicar/num1/num2/
def multiplica(request,num1, num2):
    val1 = int(num1)
    val2 = int(num2)
    result = "El resultado de la multiplicacion: %s" % (val1*val2)
    return HttpResponse(result)