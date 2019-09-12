from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from sto_bi.models import XyUsers,StoEmployee
from django.db.models import *
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
from sto_bi.serializer import XyUsersSerializers,StoEmployeeSerializers
from rest_framework import viewsets, filters, pagination
from django.shortcuts import render, redirect, HttpResponse

@api_view(['GET', 'POST'])
def getlist(request, format=None):
    if request.method == 'GET':
        meizis = XyUsers.objects.all()
        serializer = XyUsersSerializers(meizis, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = XyUsersSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#自定义分页类
class MyPageNumberPagination(PageNumberPagination):
    #每页显示多少个
    page_size = 3
    #默认每页显示3个，可以通过传入pager1/?page=2&size=4,改变默认每页显示的个数
    page_size_query_param = "size"
    #最大页数不超过10
    max_page_size = 10
    #获取页码数的
    page_query_param = "page"


class Pager1View(APIView):
    def get(self,request,*args,**kwargs):
        #获取所有数据
        roles = StoEmployee.objects.all()
        #创建分页对象，这里是自定义的MyPageNumberPagination
        pg = MyPageNumberPagination()
        #获取分页的数据
        page_roles = pg.paginate_queryset(queryset=roles,request=request,view=self)
        #对数据进行序列化
        ser = StoEmployeeSerializers(instance=page_roles,many=True)
        return Response(ser.data)





