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
    # dataList = [ { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "3.3v", "Physical": "1" } }, { "value": "", "mode": "", "names": { "Physical": "2", "Name": "5v", "wPi": "", "BCM": "" } }, { "value": "1", "mode": "IN", "names": { "BCM": "2", "wPi": "8", "Name": "SDA.1", "Physical": "3" } }, { "value": "", "mode": "", "names": { "Physical": "4", "Name": "5v", "wPi": "", "BCM": "" } }, { "value": "1", "mode": "IN", "names": { "BCM": "3", "wPi": "9", "Name": "SCL.1", "Physical": "5" } }, { "value": "", "mode": "", "names": { "Physical": "6", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "1", "mode": "IN", "names": { "BCM": "4", "wPi": "7", "Name": "GPIO. 7", "Physical": "7" } }, { "value": "0", "mode": "OUT", "names": { "Physical": "8", "Name": "TxD", "wPi": "15", "BCM": "14" } }, { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "0v", "Physical": "9" } }, { "value": "0", "mode": "OUT", "names": { "Physical": "10", "Name": "RxD", "wPi": "16", "BCM": "15" } }, { "value": "0", "mode": "IN", "names": { "BCM": "17", "wPi": "0", "Name": "GPIO. 0", "Physical": "11" } }, { "value": "0", "mode": "IN", "names": { "Physical": "12", "Name": "GPIO. 1", "wPi": "1", "BCM": "18" } }, { "value": "0", "mode": "IN", "names": { "BCM": "27", "wPi": "2", "Name": "GPIO. 2", "Physical": "13" } }, { "value": "", "mode": "", "names": { "Physical": "14", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "0", "mode": "IN", "names": { "BCM": "22", "wPi": "3", "Name": "GPIO. 3", "Physical": "15" } }, { "value": "0", "mode": "IN", "names": { "Physical": "16", "Name": "GPIO. 4", "wPi": "4", "BCM": "23" } }, { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "3.3v", "Physical": "17" } }, { "value": "0", "mode": "IN", "names": { "Physical": "18", "Name": "GPIO. 5", "wPi": "5", "BCM": "24" } }, { "value": "0", "mode": "IN", "names": { "BCM": "10", "wPi": "12", "Name": "MOSI", "Physical": "19" } }, { "value": "", "mode": "", "names": { "Physical": "20", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "0", "mode": "IN", "names": { "BCM": "9", "wPi": "13", "Name": "MISO", "Physical": "21" } }, { "value": "0", "mode": "IN", "names": { "Physical": "22", "Name": "GPIO. 6", "wPi": "6", "BCM": "25" } }, { "value": "0", "mode": "IN", "names": { "BCM": "11", "wPi": "14", "Name": "SCLK", "Physical": "23" } }, { "value": "0", "mode": "IN", "names": { "Physical": "24", "Name": "CE0", "wPi": "10", "BCM": "8" } }, { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "0v", "Physical": "25" } }, { "value": "1", "mode": "IN", "names": { "Physical": "26", "Name": "CE1", "wPi": "11", "BCM": "7" } }, { "value": "1", "mode": "IN", "names": { "BCM": "0", "wPi": "30", "Name": "SDA.0", "Physical": "27" } }, { "value": "1", "mode": "IN", "names": { "Physical": "28", "Name": "SCL.0", "wPi": "31", "BCM": "1" } }, { "value": "1", "mode": "IN", "names": { "BCM": "5", "wPi": "21", "Name": "GPIO.21", "Physical": "29" } }, { "value": "", "mode": "", "names": { "Physical": "30", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "1", "mode": "IN", "names": { "BCM": "6", "wPi": "22", "Name": "GPIO.22", "Physical": "31" } }, { "value": "0", "mode": "IN", "names": { "Physical": "32", "Name": "GPIO.26", "wPi": "26", "BCM": "12" } }, { "value": "0", "mode": "IN", "names": { "BCM": "13", "wPi": "23", "Name": "GPIO.23", "Physical": "33" } }, { "value": "", "mode": "", "names": { "Physical": "34", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "0", "mode": "IN", "names": { "BCM": "19", "wPi": "24", "Name": "GPIO.24", "Physical": "35" } }, { "value": "0", "mode": "IN", "names": { "Physical": "36", "Name": "GPIO.27", "wPi": "27", "BCM": "16" } }, { "value": "0", "mode": "IN", "names": { "BCM": "26", "wPi": "25", "Name": "GPIO.25", "Physical": "37" } }, { "value": "0", "mode": "IN", "names": { "Physical": "38", "Name": "GPIO.28", "wPi": "28", "BCM": "20" } }, { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "0v", "Physical": "39" } }, { "value": "0", "mode": "IN", "names": { "Physical": "40", "Name": "GPIO.29", "wPi": "29", "BCM": "21" } } ]
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
    if (value != 'HIGH' and value != 'LOW'):
        return HttpResponse(json.dumps({"success": False, "msg": "Value should be 'HIGH' or 'LOW' only"}, indent=4))
    elif (direction == 'IN'): # in will not set value
        return HttpResponse(json.dumps(json.dumps({"success": True}, indent=4), indent=4))
    else:
        if (value == 'HIGH'):
            GPIO.output(boardID, GPIO.HIGH)
        elif (value == 'LOW'):
            GPIO.output(boardID, GPIO.LOW)

    response = {"success": True}
    return HttpResponse(json.dumps(response, indent=4))