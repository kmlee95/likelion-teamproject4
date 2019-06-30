from django.contrib import admin
from django.urls import path
import baseProject.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', baseProject.views.base, name='base'),
]
