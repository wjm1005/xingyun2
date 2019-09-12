import json

from django.core.paginator import Paginator
from django.db.models import *
from django.shortcuts import render
from django.http import HttpResponse
from sto_bi.models import XyCusSend
def initCusSend(request):
    return render(request, 'cus_send.html')


def getCusSend(request):
    # 总记录数
    ncount = XyCusSend.objects.all().count()

    pages = request.GET['page']
    pageSize = request.GET['limit']
    weidu = request.GET['weidu']
    duliang= request.GET['duliang']

    filters = ['cus_name','weight_section','dep_name','date_time','ticket_number',
               'weight','turnover','avg_weight','avg_weight_price','avg_day_ticket','avg_day_turnover'
               ,'avg_day_weight','avg_ticket_price']

    filters = []

    for i in weidu:
        if i =='1':
            filters.append('cus_name')
        elif i == '2':
            filters.append('weight_section')
        elif i == '3':
            filters.append('dep_name')
        elif i == '4':
            filters.append('date_time')

    for i in duliang:
        if i == '1':
            filters.append('ticket_number')
        elif i == '2':
            filters.append('weight')
        elif i == '3':
            filters.append('turnover')
        elif i == '4':
            filters.append('avg_weight')
        elif i == '5':
            filters.append('avg_weight_price')
        elif i == '6':
            filters.append('avg_day_ticket')
        elif i == '7':
            filters.append('avg_day_turnover')
        elif i == '8':
            filters.append('avg_day_weight')
        elif i == '9':
            filters.append('avg_ticket_price')

    cusSend = XyCusSend.objects.values(*filters)

    SendList = []

    for item in cusSend:
        data = {
            'cus_name': item.get('cus_name'),
            'weight_section': item.get('weight_section'),
            'dep_name': item.get('dep_name'),
            'date_time': item.get('date_time'),
            'ticket_number': item.get('ticket_number'),
            'weight': item.get('weight'),
            'turnover': item.get('turnover'),
            'avg_weight': item.get('avg_weight'),
            'avg_weight_price': item.get('avg_weight_price'),
            'avg_day_ticket': item.get('avg_day_ticket'),
            'avg_day_turnover': item.get('avg_day_turnover'),
            'avg_day_weight': item.get('avg_day_weight'),
            'avg_ticket_price': item.get('avg_ticket_price')
        }

        SendList.append(data)


    paginator = Paginator(SendList,pageSize)
    #page = request.GET['page']


    list = paginator.page(pages)



    return HttpResponse(json.dumps({'rows': list.object_list,'total': ncount}),content_type="application/json")


def GetSendAnalyseByTop(request):


    # 总客户数
    nums = 0
    cus_nums = XyCusSend.objects.values('cus_name').annotate(cus_count =Count('cus_name'))
    for i in cus_nums:
        nums += 1

    #求出每个客户的总票数
    cus_nums = XyCusSend.objects.values('cus_name').annotate(CusCount=Sum('ticket_number'))
    count0 = 0
    count51 = 0
    count501 = 0
    count2001 = 0
    count5000 = 0
    for item in cus_nums:
        if item.get('CusCount')//4 <= 50 :
            count0 +=1
        elif item.get('CusCount')//4 <= 500 :
            count51+=1
        elif item.get('CusCount')//4 <= 2000 :
            count501+=1
        elif item.get('CusCount')//4 <= 5000 :
            count2001+=1
        else:
            count5000+=1
    # 各区间的客户数
    cus_ticket_nums =[count0,count51,count501,count2001,count5000]

    cus_percentage = []
    for item in cus_ticket_nums:
        cus_percentage.append((item/nums)*100)


    # 总票件量
    ticket_nums = 0
    # 各阶段票件量
    ticket_section_nums = XyCusSend.objects.values('test').annotate(ticket_sum = Sum('ticket_number'))
    for item in ticket_section_nums:
        ticket_nums = item.get('ticket_sum')

    ticket0 = 0
    ticket51 = 0
    ticket501 = 0
    ticket2001 = 0
    ticket5000 = 0

    ticket = XyCusSend.objects.values('test').filter(ticket_number__lte=50).annotate(ticket_sum = Sum('ticket_number'))
    for item in ticket:
        ticket0 = item.get('ticket_sum')/ticket_nums

    ticket = XyCusSend.objects.values('test').filter(ticket_number__lte=500,ticket_number__gt=50).annotate(ticket_sum=Sum('ticket_number'))
    for item in ticket:
        ticket51 = item.get('ticket_sum')/ticket_nums

    ticket = XyCusSend.objects.values('test').filter(ticket_number__lte=2000,ticket_number__gt=500).annotate(ticket_sum=Sum('ticket_number'))
    for item in ticket:
        ticket501 = item.get('ticket_sum')/ticket_nums

    ticket = XyCusSend.objects.values('test').filter(ticket_number__lte=5000,ticket_number__gt=2000).annotate(ticket_sum=Sum('ticket_number'))
    for item in ticket:
        ticket2001 = item.get('ticket_sum')/ticket_nums
    ticket = XyCusSend.objects.values('test').filter(ticket_number__gt=5000).annotate(ticket_sum=Sum('ticket_number'))
    for item in ticket:
        ticket5000 = item.get('ticket_sum')/ticket_nums

    ticket_percentage = [ticket0*100,ticket51*100,ticket501*100,ticket2001*100,ticket5000*100]


    #'''
    weight_section_count = XyCusSend.objects.values('weight_section').annotate(ticketCount=Sum('ticket_number'))

    weight_section_data = []
    for weight_section in weight_section_count:
        ss = {
            "ticketCount": weight_section.get('ticketCount'),
            "weight_section": weight_section.get('weight_section'),


        }
        weight_section_data.append(ss)
    weight_ticket0 = 0
    weight_ticket03 = 0
    weight_ticket05 = 0
    weight_ticket1 = 0
    weight_ticket3 = 0
    weight_ticket5 = 0
    weight_ticket8 = 0

    for item in weight_section_data:
        if item.get('weight_section')=='0-0.3':
            weight_ticket0 += item.get('ticketCount')
        if item.get('weight_section')=='0.31-0.5':
            weight_ticket03 += item.get('ticketCount')
        if item.get('weight_section')=='0.51-1':
            weight_ticket05 += item.get('ticketCount')
        if item.get('weight_section')=='1.01-2'or item.get('weight_section')=='2.01-3':
            weight_ticket1 += item.get('ticketCount')
        if item.get('weight_section')=='3.01-4'or item.get('weight_section')=='4.01-5':
            weight_ticket3 += item.get('ticketCount')
        if item.get('weight_section')=='5.01-8':
            weight_ticket5 += item.get('ticketCount')
        if item.get('weight_section')=='8.01-10'or item.get('weight_section')=='10.01-15'or item.get('weight_section')=='15.01-20'or item.get('weight_section')=='20.01-30'\
                or item.get('weight_section')=='30.01-40'or item.get('weight_section')=='40.01-50'or item.get('weight_section')=='50.01 以上':
            weight_ticket8 += item.get('ticketCount')


    weight_ticket_percentage = [
        (weight_ticket0 / ticket_nums) * 100,
        (weight_ticket03 / ticket_nums) * 100,
        (weight_ticket05 / ticket_nums) * 100,
        (weight_ticket1 / ticket_nums) * 100,
        (weight_ticket3 / ticket_nums) * 100,
        (weight_ticket5 / ticket_nums) * 100,
        (weight_ticket8 / ticket_nums) * 100
    ]


    cus_count = XyCusSend.objects.all().count()#总客户数
    weight_cus_section = XyCusSend.objects.values('weight_section').annotate(cusCount=Count('cus_name'))#客户区间

    weight_cus0 =0
    weight_cus03 = 0
    weight_cus05 = 0
    weight_cus1 = 0
    weight_cus3 = 0
    weight_cus5 = 0
    weight_cus8 = 0
    for item in weight_cus_section:
        if item.get('weight_section')=='0-0.3':
            weight_cus0 += item.get('cusCount')
        if item.get('weight_section')=='0.31-0.5':
            weight_cus03 += item.get('cusCount')
        if item.get('weight_section')=='0.51-1':
            weight_cus05 += item.get('cusCount')
        if item.get('weight_section')=='1.01-2'or item.get('weight_section')=='2.01-3':
            weight_cus1 += item.get('cusCount')
        if item.get('weight_section')=='3.01-4'or item.get('weight_section')=='4.01-5':
            weight_cus3 += item.get('cusCount')
        if item.get('weight_section')=='5.01-8':
            weight_cus5 += item.get('cusCount')
        if item.get('weight_section')=='8.01-10'or item.get('weight_section')=='10.01-15'or item.get('weight_section')=='15.01-20'or item.get('weight_section')=='20.01-30'\
                or item.get('weight_section')=='30.01-40'or item.get('weight_section')=='40.01-50'or item.get('weight_section')=='50.01 以上':
            weight_cus8 += item.get('cusCount')

    weight_cus_percentage = [
        (weight_cus0 / cus_count) * 100,
        (weight_cus03 / cus_count) * 100,
        (weight_cus05 / cus_count) * 100,
        (weight_cus1 / cus_count) * 100,
        (weight_cus3 / cus_count) * 100,
        (weight_cus5 / cus_count) * 100,
        (weight_cus8 / cus_count) * 100,
    ]

    num= {
        'section_list':['0-50','51-500','501-2000','2001-5000','>5000'],
        'cus_ticket_nums':cus_ticket_nums,# 各区间的客户数
        'ticket_percentage':ticket_percentage,#票件量占比
        'cus_percentage':cus_percentage,#客户数占比
        'weight_section_list':['0-0.3kg','0.31-0.5kg','0.5-1kg','1.01-3kg','3.01-5kg','5.01-8kg','>8kg'],
        'weight_ticket_percentage':weight_ticket_percentage,#重量区间票件量占比
        'weight_cus_percentage':weight_cus_percentage,#重量区间客户占比
    }
    return HttpResponse(json.dumps(num))

