from django.urls import path

from book2.views import index, goods, post_home, get_home, register, json_data, goods2, set_cookie, get_cookie, \
    delete_cookie, set_session, get_session, clear_session, delete_session

urlpatterns = [
    path("index/", index),
    path("<int:cat_id>/<phone:goods_id>/", goods2),
    path("<int:cat_id>/<int:goods_id>/", goods),
    # path("<cat_id>/<goods_id>/", goods),
    path("get_home/", get_home),  # 查询字符串
    path("post_home/", post_home),  # 查询字符串
    path("register/", register),
    path("json/", json_data),
    path("set_cookie/", set_cookie),
    path('get_cookie/', get_cookie),
    path('delete_cookie/', delete_cookie),
    path('set_session/', set_session),
    path('get_session/', get_session),
    path('clear_session/', clear_session),
    path('delete_session/', delete_session),
]
