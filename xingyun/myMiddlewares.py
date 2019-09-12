from django.shortcuts import HttpResponse,redirect
from django.utils.deprecation import MiddlewareMixin
'''

class md1(MiddlewareMixin):

    def process_request(self,request):

        if 'login' in request.path :
            print('去登录页面')

        elif  'api' in request.path:
            print('api')
        else:
            if request.session.get('is_login')=='1':
                print('验证通过')

            else:
                return redirect('/login/')

    def process_response(self,request,response):
        print("md1返回")
        return response
'''
