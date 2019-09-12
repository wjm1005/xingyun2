from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from sto_bi.serializer import XyUsersSerializers,StoEmployeeSerializers
from rest_framework.views import APIView
from sto_bi.models import StoEmployee
from rest_framework import viewsets
class empApi(viewsets.ModelViewSet):
        queryset = StoEmployee.objects.all()
        serializer_class = StoEmployeeSerializers
        permission_classes = []

class listEmp(APIView):
        def get(self,request,foramt=None):
                listemps = StoEmployee.objects.all()
                listName = [emp.emp_name for emp in listemps]
                return Response(listName)