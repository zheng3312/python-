from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def index(request,value1,value2):
#     # print(value1,value2)
#     # return HttpResponse(index)
#
# #
# def index (request):
#     return HttpResponse('index')
#     result = request.GET
#     username=result['username']
#     password = result.getlist('password')
#
#     print(username,password[1])

    # data1 = request.POST
    # print(data1)
    # data2 = request.body
    # print(data2)
    # return HttpResponse(index)
# def set_cookie(request):
#
#     #1. 先判断有没有cookie信息
#     # 先假设就是没有
#
#     #2.获取用户名
#     username=request.GET.get('username')
#     #3. 因为我们假设没有cookie信息,我们服务器就要设置cookie信息
#     response = HttpResponse('set_cookie')
#
#     # key,value
#     response.set_cookie('username',username)
#
#
#     #4.返回相应
#     return response


def set_cookie(request):
    username = request.GET.get('username')
    response = HttpResponse('set_cookie')
    response.set_cookie('username',username)
    return response

def get_cookie(request):
    cookies = request.COOKIES
    uesrname = cookies.get('username')
    return HttpResponse('get_cookies')

def set_session(request):
    print(request.COOKIES)
    user_id = 66666
    request.session['user_id']=user_id
    return HttpResponse('set_session')


from django.views import View
class LoginView(View):
    def get(self,request):
        return HttpResponse('登陆界面展示')
    def post(self,requdst):
        return HttpResponse('登陆的验证``````')


class HomeView(View):
    def get(self,request):
        username = request.GET.get('username')
        context ={
            'username':username,
            'age':18,
            'birthday':datetime.now,
            'friends':['tom','jack','rose',],
            'money':{
                '2019':12000,
                '2020':15000,
                '2021':22000,
            }
        }
        # return render(request, 'base.html')
        return render(request,'detail.html')
        return render(request,'index.html',context=context)




























