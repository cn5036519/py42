from django.urls import path

from book2.views import index, goods, post_home, get_home

urlpatterns = [
    path("index/", index),
    path("<cat_id>/<goods_id>/", goods),
    path("get_home/", get_home),  # 查询字符串
    path("post_home/", post_home),  # 查询字符串
]