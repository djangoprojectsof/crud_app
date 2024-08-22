from django.contrib import admin
from django.urls import path
from crud import views
urlpatterns = [
    path('',views.addshow,name='addshow' ),
]