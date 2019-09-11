from django.http import HttpResponse
from django.shortcuts import render
import json
import os

from . import processGOIPStatus
from . import GOIPStatus
from .MyEncoder import MyEncoder

import RPi.GPIO as GPIO 

def getGOIPStatusData():
    output = os.popen('gpio readall')
    gpioStatusString = output.read()
    dataList = processGOIPStatus.parseGOIPStatusData(gpioStatusString)
    return dataList

def gpio_overview(request):
    # print(GPIO.RPI_INFO)
    dataList = getGOIPStatusData()
    return HttpResponse(json.dumps(dataList, cls=MyEncoder, indent=4))

def gpio_setPinStatus(request):
    GPIO.setmode(GPIO.BOARD)

    boardID = int(request.GET.get('boardID'))
    pinList = getGOIPStatusData()
    if (boardID == None):
        return HttpResponse(json.dumps({"success": False, "msg": "Board ID is mandatory"}, indent=4))
    else:
        isProperPin = False
        for pin in pinList:
            if (pin.getPinID() == boardID):
                isProperPin = True
                break
        if (isProperPin == False):
             return HttpResponse(json.dumps({"success": False, "msg": "Board ID %s is not valid" %(boardID)}, indent=4))
    
    direction = request.GET.get('direction')
    if (direction == 'IN'):
        GPIO.setup(boardID, GPIO.IN)
    elif (direction == 'OUT'):
        GPIO.setup(boardID, GPIO.OUT)
    else:
        return HttpResponse(json.dumps({"success": False, "msg": "Direction should be IN or OUT only"}, indent=4))

    value = request.GET.get('value')
    if (value != 'HIGH' or value != 'LOW'):
        return HttpResponse(json.dumps({"success": False, "msg": "Value should be 'HIGH' or 'LOW' only"}, indent=4))
    else:
        if (value == 'HIGH'):
            GPIO.output(boardID, GPIO.HIGH)
        elif (value == 'LOW'):
            GPIO.output(boardID, GPIO.LOW)

    response = {"success": True}
    return HttpResponse(json.dumps(response, indent=4))