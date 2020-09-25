import json

from django.http import HttpResponse
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
    return HttpResponse("json")


def goods2(request, cat_id, goods_id):
    print(goods_id, type(goods_id))
    return HttpResponse("Goods2")