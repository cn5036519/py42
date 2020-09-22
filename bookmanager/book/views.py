from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("ok")

def center(request):
    # 将上下文交给模板进行处理,处理后将视图响应给客户端.
    return render(request, "book/center.html", {'title': "center页面"})