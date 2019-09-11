from django.http import HttpResponse
from django.shortcuts import render
import json
import os

from . import processGOIPStatus
from . import GOIPStatus
from .MyEncoder import MyEncoder

def gpio_overview(request):
    # print(GPIO.RPI_INFO)
    output = os.popen('gpio readall')
    gpioStatusString = output.read()
    dataList = processGOIPStatus.parseGOIPStatusData(gpioStatusString)
    return HttpResponse(json.dumps(dataList, cls=MyEncoder, indent=4))

def gpio_setPinStatus(request):
    response = {"success": True}
    command = 'response["success"]=False\nprint(json.dumps(response))'
    exec(command)
    # response = {
    #     'success': True
    # }
    return HttpResponse(json.dumps(response, indent=4))