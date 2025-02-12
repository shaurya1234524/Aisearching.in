from django.contrib import admin
from django.urls import path
from aiexporiahome import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

path('',views.display,name="display"),
path('form.html',views.form,name="form")
]
