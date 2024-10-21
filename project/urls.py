"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path , include
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainpage),   # url 경로를 ''로 지정하고 mainpage view와 연결함.  , 127.0.0.1:8080에 들어가면 mainpage view와 연결이 됨.
                            
    path('api/get-gpt-response/', get_gpt_response, name='get_gpt_response'),
    path('test', mainpage_2, name='test'),
    path('search/', include('search.urls')),
    path('search/Product', Product_page, name='Product')
]
