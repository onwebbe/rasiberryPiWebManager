from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def login(request):
  loginData = {
    'id': "4291d7da9005377ec9aec4a71ea837f",
    'name': 'onwebbe',
    'username': 'admin',
    'password': '',
    'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/jZUIxmJycoymBprLOUbT.png',
    'status': 1,
    'telephone': '',
    'lastLoginIp': '27.154.74.117',
    'lastLoginTime': 1534837621348,
    'creatorId': 'admin',
    'createTime': 1497160610259,
    'deleted': 0,
    'roleId': 'admin',
    'lang': 'zh-CN',
    'token': '4291d7da9005377ec9aec4a71ea837f'
  }
  return HttpResponse(json.dumps(loginData, indent=4))

def step2code(request):
  stepData = {"stepCode": 1}
  return HttpResponse(json.dumps(stepData, indent=4))