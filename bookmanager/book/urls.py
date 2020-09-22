from django.urls import path

from book.views import index, center

urlpatterns = [
    path('index/', index),
    path('center/', center)

]