"""dreamaryproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

# views.py 파일 연결
from page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # '' url이 들어오면 views.py의 home 함수 실행를 실행시킬거고, 이 path를 home이라고 부를거야! ^0^
    path('', views.home, name = "home"),
]
