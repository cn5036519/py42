from django.db import models

# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=10, verbose_name="书名")
    pub_date = models.DateField(null=True, verbose_name="出版日期")
    readcount = models.IntegerField(default=0, verbose_name="阅读量")
    commentcount = models.IntegerField(default=0, verbose_name="评论量")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "bookinfo"
        verbose_name = "书籍"


class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        ('1', "男"),
        ('2', "女"),
        ('3', "未知"),
    )
    name = models.CharField(max_length=10, verbose_name="姓名")
    # smallint
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=3, verbose_name="性别")
    description = models.CharField(max_length=100, null=True, verbose_name="描述信息")
    # tinyint
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")
    book = models.ForeignKey(to=BookInfo, on_delete=models.CASCADE, verbose_name="书籍")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "peopleinfo"
        verbose_name = "人物"


