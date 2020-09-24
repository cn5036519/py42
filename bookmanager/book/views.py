from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from book.models import BookInfo


def index(request):
    return HttpResponse("ok")

def center(request):
    # 将上下文交给模板进行处理,处理后将视图响应给客户端.
    return render(request, "book/center.html", {'title': "center页面"})


if __name__ == '__main__':

    # 查询编号为1的图书
    BookInfo.objects.get(id=1)
    # 查询书名包含'湖'的图书
    BookInfo.objects.filter(name__contains="湖")
    # 查询书名以'部'结尾的图书
    BookInfo.objects.filter(name__endswith="部")
    # 查询书名为空的图书
    BookInfo.objects.filter(name__isnull=True)
    # 查询编号为1或3或5的图书
    BookInfo.objects.filter(id__in=(1,3,5))
    BookInfo.objects.filter(id__in=[1,3,5])
    # 查询编号大于3的图书
    BookInfo.objects.filter(pk__gt=3)
    # 查询1980年发表的图书
    BookInfo.objects.filter(pub_date__year="1980")
    # 查询1990年1月1日后发表的图书
    BookInfo.objects.filter(pub_date__gt="1990-1-1")
    BookInfo.objects.filter(pub_date__gt="1990-01-01")

    # 查询阅读量大于等于评论量的图书
    BookInfo.objects.filter(readcount__gte=F("commentcount"))
    # 查询阅读量大于2倍评论量的图书
    BookInfo.objects.filter(readcount__gt=F("commentcount")*2)
    # 查询阅读量大于20，并且编号小于3的图书
    BookInfo.objects.filter(readcount__gt=20, id__lt=3)
    BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
    BookInfo.objects.filter(Q(readcount__gt=20)&Q(pk__lt=3))
    # 查询阅读量大于20的图书
    BookInfo.objects.filter(readcount__gt=20)
    # 查询阅读量大于20，或编号小于3的图书
    BookInfo.objects.filter(Q(readcount__gt=20)|Q(pk__lt=3))
    # 查询编号不等于3的图书
    BookInfo.objects.exclude(id=3)
    BookInfo.objects.filter(~Q(id=3))
    BookInfo.objects.filter(Q(id__gt=3)|Q(id__lt=3))