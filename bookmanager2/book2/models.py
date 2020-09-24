from django.db import models

class BookInfo(models.Model):
    # 创建字段，字段类型...
    name = models.CharField(max_length=10, verbose_name='名称')
    pub_date = models.DateField(verbose_name='发布日期',null=True)
    readcount = models.IntegerField(default=0, verbose_name='阅读量')
    commentcount = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'bookinfo'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称
        verbose_name_plural = '图书们'

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name


# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (1, '男'),
        (2, '女'),
        (3, '未知'),
    )
    name = models.CharField(max_length=10, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=3, verbose_name='性别')
    description = models.CharField(max_length=100, null=True, verbose_name='描述信息')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物'
        verbose_name_plural = '人物们'

    def __str__(self):
        return self.name
