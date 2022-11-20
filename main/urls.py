from django.urls import path, include
from django.contrib import admin
from . import views as v


app_name = 'project'

urlpatterns = [
    path('', v.index, name='index'),
]
