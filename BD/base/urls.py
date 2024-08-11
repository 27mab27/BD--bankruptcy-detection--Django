from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('',views.homePage,name="home"),
    path('table',views.table,name="table"),
    path('OurModel',views.ourModel,name="OurModel")

    
]
