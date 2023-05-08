from django.contrib import admin
from django.urls import path, include
from Rapid7ToneDetermination import views

urlpatterns = [
    path('Rapid7ToneDetermination/', views.RapidUserInfo.as_view()),
    path('RapidUploadFile/', views.RapidUnloadFile.as_view()),
    path('RapidGetFile/', views.RapidGetFile.as_view())
]