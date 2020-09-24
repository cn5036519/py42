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
    return HttpResponse("get_home")

def post_home(request):
    # 接收的是表单数据
    print(request.POST)
    # 接收的是查询字符串
    print(request.GET)
    return HttpResponse("post_home")