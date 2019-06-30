from django.contrib import admin
from django.urls import path
import kindAnimal.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', kindAnimal.views.kindAnimal, name='kindAnimal'),
]
