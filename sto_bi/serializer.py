from rest_framework import serializers
from .models import XyUsers,StoEmployee


class XyUsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = XyUsers  # 指定的模型类
        fields = ('id', 'user_name', 'user_password', 'user_power',)

class StoEmployeeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StoEmployee  # 指定的模型类
        fields = ('emp_id', 'emp_name', 'emp_idcard', 'emp_sex','emp_phone','emp_address','emp_address',)
