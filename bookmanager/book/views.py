from django.core.paginator import Paginator
from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from book.models import BookInfo, PeopleInfo


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

    # 查询书籍为1的所有人物信息
    PeopleInfo.objects.filter(book_id=1)
    book = BookInfo.objects.get(id=1)
    book.peopleinfo_set.all()
    # 查询人物为1的书籍信息
    BookInfo.objects.filter(peopleinfo__id=1)
    people = PeopleInfo.objects.get(id=1)
    people.book.name

    # 查询图书，要求图书人物为"郭靖"
    BookInfo.objects.filter(peopleinfo__name="郭靖")
    # 查询图书，要求图书中人物的描述包含"八"
    BookInfo.objects.filter(peopleinfo__description__contains="八")

    # 查询书名为“天龙八部”的所有人物
    PeopleInfo.objects.filter(book__name="天龙八部")
    # 查询图书阅读量大于30的所有人物
    PeopleInfo.objects.filter(book__readcount__gt=30)


    PeopleInfo.objects.count()
    # 返回值为一个people实例对象
    PeopleInfo.objects.create(
        name="薛婷婷",
        gender=2,
        book_id=1
    )
    PeopleInfo.objects.create(
        name="王同培",
        gender=1,
        # book必须是个实例对象
        book=BookInfo.objects.get(id=1)
    )

    people = PeopleInfo(
        name="单晚霞",
        gender=2,
        book_id=1
    )
    people.save()

    people = PeopleInfo.objects.get(name="单晚霞")
    people.book_id = 2
    people.save()

    # 返回影响的数据行数
    PeopleInfo.objects.filter(name="单晚霞").update(book_id=1)

    # 返回值:(<PeopleInfo: 张太帅>, True),第二个元素表示是否创建了一个新对象.
    PeopleInfo.objects.update_or_create(book_id=3, name="张太帅")
    # 如果对象不存在,使用默认值创建一个.如果对象存在,则再创建一个新的对象.
    PeopleInfo.objects.update_or_create(book_id=1, name="张太帅")

    # 返回值:(1, {'book.PeopleInfo': 1}) ->book指应用名
    PeopleInfo.objects.get(name="单晚霞").delete()
    PeopleInfo.objects.filter(name="张太帅").delete()

#     分页
    peoples = PeopleInfo.objects.all()
    paginator = Paginator(peoples, 5)   # 每页5条数据
    # 返回有效页:<Page 1 of 4>
    paginator.get_page(1)
    # 返回总页数
    paginator.num_pages
    # 返回有效页:<Page 1 of 4>, 与get_page(num)的区别是:num如果不是有效数字,就会报错.
    page = paginator.page(1)
    # 返回值:QuerySet
    page.object_list
    page.has_next()
    page.has_previous()
    page.has_other_pages()
    page.next_page_number() # 下一页是第几页
    page.previous_page_number() # 上一页是第几页

