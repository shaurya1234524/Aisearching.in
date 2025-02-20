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
from aiexporiahome.views import robots_txt,sitemap
urlpatterns = [
    path('admin/', admin.site.urls),
    path('uploadAI',views.uploadAI,name="uploadAI"),
    path('blo',views.blo,name="blo"),
    path('',include(aiexporiahome.urls)),
    path('india',views.displayin,name="displayin"),
    path('NewAi',views.NewAi,name="NewAi"),
    path('code',views.code,name="code"),
    path('MusicsAi',views.MusicsAi,name="MusicsAi"),
    path('Imagegen',views.Imagegen,name="Imagegen"),
    path('VideoGeneration',views.VideoGeneration,name="VideoGeneration"),
    path('Study',views.Study,name="Study"),
    path('chatbot',views.chatbot,name="chatbot"),
    path('Buisnesses',views.buisnesses,name="Buisnesses"),
    path('increase-like/<int:ai_id>', views.increase_like, name='increase_like'),
    path('HomeworkAi',views.HomeworkAi,name="HomeworkAi"),
  path('sitemap.xml',views.sitemap,name="sitemap"),
 path("robots.txt", views.robots_txt, name="robots_txt"),
  path("ai-analysis/<str:tool_name>",views.analyzing,name="analyzing"),
 path("ai-analysis/<str:tool_name>",views.ai_tool_analysis,name="ai_tool_analysis"),
    path('searchresult',views.searchresults,name="searchresults"),
    path('searchres',views.searchres,name="searchres"),
    path('searchresultsss',views.searchresultsss,name="searchresultsss"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

  

