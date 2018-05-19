from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from . import views



urlpatterns = [
    path('', views.show_data, name='data'),

]
