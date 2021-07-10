from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="home"),
    path('add', views.add, name="add"),
    path('q', views.book_list, name="filter"),
]