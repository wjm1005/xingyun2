import json

from django.http import HttpResponse
from django.shortcuts import render
from sto_bi.models import XyUsers


def initUserManage(request):


    return render(request, 'user_manage.html')

def getUser(requset):
    userList = XyUsers.objects.all()

    data = []
    for item in userList:
        user = {
            'id':item.id,
            'user_name':item.user_name
        }
        data.append(user)


    return HttpResponse(json.dumps(data))