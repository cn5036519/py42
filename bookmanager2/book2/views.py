import datetime
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("index")

# 关键字传参,所以参数位置随意放
def goods(request, goods_id, cat_id):
    print(cat_id, goods_id)
    return HttpResponse("goods")

def get_home(request):
    queryDict = request.GET
    # <QueryDict: {'name': ['jack'], 'age': ['34']}>
    print(queryDict)
    uname = queryDict.get("name")
    uage = queryDict["age"]
    print(uname, uage)
    print(queryDict.getlist("name"))  # ['jack', 'lucy']
    # 表示提交的数据的编码格式. 返回None,表示使用浏览器的默认设置.
    print(request.encoding)
    print(request.path)
    print(request.path_info)
    print(request.get_full_path())  # /get_home/?name=jack&age=45&name=lucy
    print(request.META.get("CONTENT_TYPE"))  # text/plain
    return HttpResponse("get_home")

def post_home(request):
    # 接收的是表单数据
    print(request.POST)
    # 接收的是查询字符串
    print(request.GET)
    print(request.META.get("CONTENT_TYPE"))  # text/plain
    return HttpResponse("post_home")

def register(request):
    # 接收表单数据
    print(request.POST)
    print(request.META.get("CONTENT_TYPE"))  # multipart/form-data; boundary=--------------------------858659475380648841666494
    return HttpResponse("register")

def json_data(request):
    # 接收json数据,bytes类型
    print(request.body.decode(encoding="utf-8"))
    # json字符串转为python数据类型
    print(json.loads(request.body.decode(encoding="utf-8")))
    # "CONTENT_TYPE" 必须全部大写.
    print(request.META.get("CONTENT_TYPE"))  # application/json
    # return HttpResponse("json")
    # 响应一个json数据
    # return JsonResponse(json.loads(request.body.decode(encoding="utf-8")))
    # 元组数据不可以序列化,但不会报错,它转为了列表.即[100, 200, 300, "2014-05-25", [1, 2]]
    return JsonResponse([100, 200, 300, datetime.date(2014,5,25), (1,2)], safe=False)
    # return JsonResponse("hahaha", safe=False)
    # 中文无法正常显示
    # return JsonResponse("哈哈哈", safe=False)


def goods2(request, cat_id, goods_id):
    print(goods_id, type(goods_id))
    # HttpResponse的第一个参数是content,即响应体,bytes类型.
    # HttpResponse的第二个参数是content_type,如果不传值,默认是'text/html'; charset='utf-8'
    # HttpResponse的第三个参数是status,如果不传值,默认是200
    response = HttpResponse("Goods2")
    # 自定义响应头
    response["School"] = "itcast"
    return response

def set_cookie(request):
    username = request.GET.get("username")
    response = HttpResponse("set_cookie")
    # cookie的本质:设置一个响应头,key为Set-Cookie,值为passwd=123456
    response.set_cookie("passwd", "123456")
    # 设置cookie的有效时间(单位:秒)
    response.set_cookie("user", username, max_age=3600)
    return response

def get_cookie(request):
    print(request.COOKIES, type(request.COOKIES))  # dict
    return HttpResponse("get_cookie")

def delete_cookie(request):
    response = HttpResponse("delete_cookie")
    # 删除cookie的本质:设置cookie的有效期为0
    response.delete_cookie("user")
    response.delete_cookie("passwd")
    return response

from django.contrib.sessions.backends.db import SessionStore

def set_session(request):
    request.session["user"] = "lucy"
    request.session["age"] = 35
    # 设置session的有效期
    request.session.set_expiry(3600)
    return HttpResponse("set_session")

def get_session(request):
    print(request.session.get("user"))
    print(request.session.get("age"))
    return HttpResponse("get_session")

def clear_session(request):
    print(request.session.get("user"))
    request.session.clear()
    print(request.session.get("user"))
    return HttpResponse("clear_session")

def delete_session(request):
    print(request.session.get("user"))
    request.session.flush()
    print(request.session.get("user"))
    return HttpResponse("delete_session")