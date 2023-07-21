from django.contrib import admin
from django.urls import path,include
from bookstore import views
urlpatterns = [
    path('',views.danh_sach, name="danh_sach"),
    path('/timsach',views.timsach, name="timsach"),
    path('capnhat/<int:sach_id>/',views.capnhat_sach,name='capnhat_sach'),
    path('xu_ly_capnhat',views.xu_ly_capnhat,name='xu_ly_capnhat'),
]

