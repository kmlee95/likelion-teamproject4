from django.contrib import admin
from django.urls import path, include
import kindAnimal.views
import mainPage.views
import animalGoods.views
import animalShop.views
import personal.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainPage.views.mainPage, name='mainPage'),
    path('kindAnimal/', kindAnimal.views.kindAnimal, name='kindAnimal'),
    path('animalGoods/', animalGoods.views.animalGoods, name='animalGoods'),
    path('animalShop/', animalShop.views.animalShop, name='animalShop'),
    path('personal/', personal.views.personal, name='personal'),
    path('personal/<int:personal_id>/', personal.views.detail, name = 'detail'),
    path('personal/write/', personal.views.write, name = 'write'),
    path('personal/create/', personal.views.create, name = 'create'),
    path('accounts/', include('accounts.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

