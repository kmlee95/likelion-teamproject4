from django.contrib import admin
from django.urls import path, include
import kindAnimal.views
import mainPage.views
import animalGoods.views
import animalShop.views
import personal.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainPage.views.mainPage, name='mainPage'),
    path('kindAnimal/', kindAnimal.views.kindAnimal, name='kindAnimal'),
    path('animalGoods/', animalGoods.views.animalGoods, name='animalGoods'),
    path('animalShop/', animalShop.views.animalShop, name='animalShop'),
    path('personal/', personal.views.personal, name='personal'),
    path('accounts/', include('accounts.urls')),
]
