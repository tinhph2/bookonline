from django.contrib import admin
from django.urls import path,include
from bookstore import views
urlpatterns = [
    path('',views.danh_sach, name="danh_sach"),
    path('/timsach',views.timsach, name="timsach"),
]
