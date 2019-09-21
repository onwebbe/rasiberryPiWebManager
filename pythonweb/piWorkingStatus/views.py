from django.shortcuts import render
from django.http import HttpResponse
import json
import math

import psutil
import sys
import os
def killProcess(request):
  PID = int(request.GET.get('PID'))
  try:
    psObject = psutil.Process(PID)
    psObject.terminate()
  except psutil.NoSuchProcess:
    return HttpResponse(json.dumps({"success": False, "msg": "Failed to kill Process %s" % (PID)}, indent=4))
  return HttpResponse(json.dumps({"success": True, "msg": ""}, indent=4))

# Create your views here.
def piStatus(request):
  piStatus = {
    'msg': '',
    'success': True,
    'result': {
      'CPUUsage': {
        'percent': str(psutil.cpu_percent(1))
      },
      'MemoryUsage': getMemoryUsage(request)
    }
    
  }
  return HttpResponse(json.dumps(piStatus, indent=4))

def getMemoryUsage(request):
  phymem = psutil.virtual_memory()
  memoryStatus = {
    'usage': str(int(phymem.used / 1024 / 1024)),
    'total': str(int(phymem.total / 1024 / 1024))
  }
  return memoryStatus

def getPiRunningStatusData(request):
  pageSize = request.GET.get('pageSize')
  pageNo = request.GET.get('pageNo')
  print ("pageSize:%s  pageNo:%s" % (pageSize, pageNo))
  if (pageSize == None):
    pageSize = 10
  else:
    pageSize = int(pageSize)
  
  if (pageNo == None):
    pageNo = 1
  else:
    pageNo = int(pageNo)

  allPIDs = psutil.pids()
  pidDataList = []
  for pid in allPIDs:
    pidDataObj = __getOneProcessor(pid)
    if (pidDataObj != None):
      pidDataList.append(pidDataObj)
  response = {
    "result": {
      "pageNo": pageNo,
      "pageSize": pageSize,
      "totalCount": len(pidDataList),
      "totalPage": math.floor(len(pidDataList) / 10),
      "data": pidDataList
    },
    "success": True,
    "msg": ''
  }
  return HttpResponse(json.dumps(response, indent=4))
  
def __getOneProcessor(pid):
  try:
    psObject = psutil.Process(pid)
    psData = {}
    command = psObject.cmdline() #['python3']
    uid = psObject.username()
    startTime = psObject.create_time()
    cpu = psObject.cpu_times() #pcputimes(user=0.081150144, system=0.053269812, children_user=0.0, children_system=0.0)
    mem = psObject.memory_info() #pmem(rss=8310784, vms=2481725440, pfaults=3207, pageins=18)
    memPercent = psObject.memory_percent()
    psData["PID"] = pid
    psData["UID"] = uid
    psData["command"] = ' '.join(command)
    time = "%s / %s" % (startTime, cpu.user)
    psData["time"] = time
    psData["mem"] = "%dM / %f%s" % (mem.rss / 1024 / 1024, round(memPercent * 100, 2), '%')
    return psData
  except psutil.NoSuchProcess:
    return None

def getDiskInformation(request):
  diskInfo = psutil.disk_usage('/')
  data = {
    "total": diskInfo.total,
    "used": diskInfo.used,
    "free": diskInfo.free,
    "percent": diskInfo.percent
  }
  return HttpResponse(json.dumps({
    "success": True,
    "msg": "",
    "result": data
  }, indent=4))