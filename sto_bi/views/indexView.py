from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from sto_bi.views.loginView import check_login

#@check_login
def index(request):
    return render(request,'index.html')

def logout(request):
    request.session.flush()  # 删除session
    return HttpResponseRedirect("/login/")