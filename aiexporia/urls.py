"""
URL configuration for aiexporia project.

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
from django.urls import path,include
import aiexporiahome.urls
from aiexporiahome import views
from django.conf import settings
from django.views.generic.base import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('uploadAI',views.uploadAI,name="uploadAI"),
    path('blo',views.blo,name="blo"),
    path('',include(aiexporiahome.urls)),
    path('india',views.displayin,name="displayin"),

    path('searchresult',views.searchresults,name="searchresults"),
    path('searchres',views.searchres,name="searchres"),
    path('searchresultsss',views.searchresultsss,name="searchresultsss"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns = [
    path('sitemap.xml', TemplateView.as_view(template_name="sitemap.xml", content_type="application/xml")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
