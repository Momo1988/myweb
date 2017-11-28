"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from online import views
from . import testdb,search
urlpatterns = [
    url(r'^thisisadminonly/', admin.site.urls),
    url(r'^online/', include('online.urls')),
    url(r'^$', views.hello),
    url(r'^testdb$', testdb.adddata),
    url(r'^getdb$', testdb.getdata),
    url(r'^updatedb', testdb.update),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post', search.search_post),


]


