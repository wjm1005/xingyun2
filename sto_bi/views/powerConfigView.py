from django.http import HttpResponse
from django.shortcuts import render
from sto_bi.models import XyMenuLevel,XyMenu,XyUsers
from django.db.models import *
import json
import string
import random
def init_powerConfig(request):



    return render(request, 'power_config.html')


def getMenuLevel(request):

    menuLevel = XyMenuLevel.objects.all()
    menuLevelList = []

    for menu in menuLevel:
        data = {
            'level_id':menu.level_id,
            'level_name':menu.level_name
        }
        menuLevelList.append(data)
    return HttpResponse(json.dumps(menuLevelList))
def getPowerUSer(request):
    # level_id = request.GET['level_id']
    level_id = 1
    user_list = XyUsers.objects.values().filter(level_id = 1)
    user_data = []

    for user in user_list:
        data = {
            'id':user.get('id'),
            'user_name':user.get('user_name')
        }
        user_data.append(data)
    return HttpResponse(json.dumps(user_data))



def getMenu(request):
    #level_id = request.GET['level_id']
    level_id = 1
    menuid_list= XyMenuLevel.objects.values().get(level_id = level_id)

    menuid_list = menuid_list['menu'].split(",")
    print(menuid_list)

    menu = XyMenu.objects.all()
    lists = []
    is_select=0#是否找到
    for menus in menu:
        for i in menuid_list:
            if menus.menu_id == int(i):
                data = {
                    'menu_id': menus.menu_id,
                    'menu_name': menus.menu_name,
                    'parent_id': menus.parent_id,
                    'menu_level': menus.menu_level,
                    'is_checkbox':'1'
                }
                is_select = 1
                break;
        if is_select == 0:
            data = {
                'menu_id':menus.menu_id,
                'menu_name':menus.menu_name,
                'parent_id':menus.parent_id,
                'menu_level': menus.menu_level,
                'is_checkbox': '0'
            }
        elif is_select == 1:
            is_select = 0
        lists.append(data)
    print(lists)

    nemu_level_1 = []
    nemu_level_2 = []
    nemu_level_3 = []

    for i in lists:
        if i['menu_level'] == 1:
            nemu_level_1.append(i)
        elif i['menu_level'] == 2:
            nemu_level_2.append(i)
        elif i['menu_level'] == 3:
            nemu_level_3.append(i)


    nemuList =[]

    for nemu1 in nemu_level_1:
        nemuList.append(nemu1)
        for nemu2 in nemu_level_2:
            if nemu1['menu_id'] == nemu2['parent_id']:
                nemuList.append(nemu2)
            for nemu3 in nemu_level_3:
                if nemu2['menu_id'] == nemu3['parent_id'] and nemu1['menu_id'] == nemu2['parent_id']:
                    nemuList.append(nemu3)

    return  HttpResponse(json.dumps(nemuList))


def addPowerRole(request):
    #roleName = request.GET['roleName']
    roleName = '决策者'

    newrole =  XyMenuLevel(level_id=2,level_name=roleName)
    newrole.save()

    data ={
        'success':'添加成功'
    }
    data2 = []
    data2.append(data)
    return HttpResponse(json.dumps(data))

def upPower(request):

    powerList = json.loads(request.GET['powerList'])
    powerStr = ''
    for power in powerList:
        powerStr = powerStr+str(power.get('menu_id'))+','
    powerStr = powerStr[:-1]

    XyMenuLevel.objects.filter(level_id=1).update(menu=powerStr)

    data = {
        'success': '授权成功'
    }
    data2 = []
    data2.append(data)
    return HttpResponse(json.dumps(data))


