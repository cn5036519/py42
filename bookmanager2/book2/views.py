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
    return JsonResponse([100, 200, 300, datetime.date(2014,5,25)], safe=False)
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