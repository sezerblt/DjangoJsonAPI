from django import views
from . import views
from django.urls import path

urlpatterns=[
    path('',views.index),
    path('departments/<int:id>',views.departmentApi),
]