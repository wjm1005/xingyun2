from django.http import HttpResponse
from django.shortcuts import render
from sto_bi.models import *
from django.db.models import *
import json
import string
import random
def init_op_data(request):


    depList = StoDepartment.objects.filter(parent_id=46)
    depLists = []
    for dep in depList:
        data = {
            "id":dep.dep_id,
            "name":dep.dep_name

        }
        depLists.append(data)
    test = '多个数据测试'
    return render(request,'op_data.html',{'data':depLists,'test':test})



def queryOrder(request):
    data = []

    #name=string.ascii_letters + string.ascii_letters +string.ascii_letters
    dl_group = request.GET['dl_group']
    operatename = str(request.GET['operatename'])
    departname = str(request.GET['departname'])
    dateTimeRange = str(request.GET['dateTimeRange'])
    type1 = str(request.GET['type1'])
    #print(dep)
    #dep_opj = StoDepartment.objects.get(dep_name='操作二组')



    #empList= dep_opj.stoemployee_set.all()
    #
    emp_data = []
    dep = '操作七组'
    emp_list2 = StoEmployee.objects.values().filter(emp_department__dep_name=dep)
    for emp in emp_list2:
        emp_data.append(emp.get('emp_name'))

    search_dict ={}
    search_dict['scantype'] = '发件'
    search_dict['scanemp__in'] = emp_data

    tiaojian = []
    for group in dl_group:
        if group == '1':
            tiaojian.append('scantype')
        elif group == '2':
            tiaojian.append('scanemp__emp_department')
        elif group == '3':
            tiaojian.append('scanemp')
    print(tiaojian)


    empList = StoWtOp.objects.values(*tiaojian).filter(**search_dict).annotate(Votescount=Count('billno'),weightCount=Sum('weight'))


    # oplist = StoWtOp.objects.filter(scanemp='谢志红')

    for empLists in empList:
        ss = {
            "scanemp__emp_department": empLists.get('scanemp__emp_department'),
            "scantype": empLists.get('scantype'),
            "scanemp": empLists.get('scanemp'),
            "Votescount": empLists.get('Votescount'),
            "weightCount": empLists.get('weightCount')
        }
        data.append(ss)



    return HttpResponse(json.dumps(data))