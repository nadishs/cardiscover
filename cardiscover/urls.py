"""cardiscover URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic.base import TemplateView
from car.views import index
from search.views import msearch
urlpatterns = [
    url(r'^$', index),                   
    url(r'^search/', include("search.urls", namespace='search')),
    url(r'^msearch/', msearch),
    url(r'^car/', include('car.urls')),
    url(r'^admin/', admin.site.urls),
   ]

