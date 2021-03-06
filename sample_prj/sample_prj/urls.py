"""sample_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from sample1 import views as sample_view

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin_view"),
    url(r'^post/', sample_view.post_view, name="post_view"),
    url(r'^success/', sample_view.success_view, name="success_view"),
    url(r'^', sample_view.form_view, name="form_view"),
]
