from django.urls import path

from book2.views import index, goods, post_home, get_home, register, json_data, goods2

urlpatterns = [
    path("index/", index),
    path("<int:cat_id>/<phone:goods_id>/", goods2),
    path("<int:cat_id>/<int:goods_id>/", goods),
    # path("<cat_id>/<goods_id>/", goods),
    path("get_home/", get_home),  # 查询字符串
    path("post_home/", post_home),  # 查询字符串
    path("register/", register),
    path("json/", json_data),
]
