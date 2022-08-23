from django.contrib import admin
from django.urls import path

from weather_puller import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index)
]
