from django.contrib import admin
from django.urls import path
import kindAnimal.views
import mainPage.views
import animalGoods.views
import animalShop.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainPage.views.mainPage, name='mainPage'),
    path('kindAnimal/', kindAnimal.views.kindAnimal, name='kindAnimal'),
    path('animalGoods/', animalGoods.views.animalGoods, name='animalGoods'),
    path('animalShop/', animalShop.views.animalShop, name='animalShop'),
]
