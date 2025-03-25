from django.contrib import admin
from django.urls import path, include
from Rapid7ToneDetermination import views

urlpatterns = [
    path('Rapid7ToneDetermination/', views.RapidUserInfo.as_view()),
    path('RapidUploadFile/', views.RapidUploadFile.as_view()),
    path('RapidGetFile/', views.RapidGetFile.as_view()),
    path('RapidUpLoadPure/', views.RpaidUploadPure.as_view()),
    path('RpaidGetNoise/', views.RpaidGetNoise.as_view()),
    path('check_task_status/<str:task_id>/', views.CheckTaskStatusView.as_view(), name='check_task_status'),
    path('check_pureImg_exist/', views.CheckIsPureResultImg.as_view()),
]