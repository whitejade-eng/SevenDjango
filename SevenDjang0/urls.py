"""SevenDjang0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from Rapid7ToneDetermination import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    # path("admin/", admin.site.urls),
#'wx/'代表是浏览器端口8000后的一级路径，‘wx_login.urls’代表的是浏览器的二级路径（二级路径是调用wx_login里面的urls.py）
    path('', include('Rapid7ToneDetermination.urls')),
    re_path(r'static/(?P<path>.*)',serve,{'document_root':settings.STATIC_ROOT}),
]

