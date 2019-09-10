from django.http import HttpResponse
from django.shortcuts import render


def gpio_overview(request):
    # print(GPIO.RPI_INFO)
    return HttpResponse('Hallo World')
