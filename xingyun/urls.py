"""xingyun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from sto_bi import views
from sto_bi.views import opDataView,indexView,loginView,apiview,empView,powerConfigView,cusSendView,userManageView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'emps', empView.empApi)
#router.register(r'listEmp', empView.listEmp)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', indexView.index),
    url(r'^templates/op_data/', opDataView.init_op_data),
    url(r'^queryOrder/$', opDataView.queryOrder),
    url(r'^login/$', loginView.login),
    url(r'^logout/$', indexView.logout),
    url(r'^api/getlist/$', apiview.getlist),
    url(r'^api/emplist/$', apiview.Pager1View.as_view()),
    url(r'^api/listEmp/$', empView.listEmp.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^powerConfig/$', powerConfigView.init_powerConfig),
    url(r'^getMenuLevel/$', powerConfigView.getMenuLevel),
    url(r'^getMenu/$', powerConfigView.getMenu),
    url(r'^getPowerUser/$', powerConfigView.getPowerUSer),
    url(r'^addPowerRole/$', powerConfigView.addPowerRole),
    url(r'^upPower/$', powerConfigView.upPower),
    url(r'^cusSend/$', cusSendView.initCusSend),
    url(r'^GetSendAnalyseByTop/$', cusSendView.GetSendAnalyseByTop),
    url(r'^initUserManage/$', userManageView.initUserManage),
    url(r'^getUser/$', userManageView.getUser),
    url(r'^getCusSend/$', cusSendView.getCusSend),



    url('',include('book_api.urls'))
]
