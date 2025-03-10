
from main.views import home, get_news, get_products
from django.contrib import admin
from django.urls import path
from main.views import home
from django.conf.urls.static import static
from django.conf import settings
from main.views import get_news, get_products, home, building_mixtures, metal_structures, about_company, contacts, cement, stone, sand, vacancies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('get-news/', get_news, name='get_news'),
    path('get-products/', get_products, name='get_products'),
    path('building-mixtures/', building_mixtures, name='building_mixtures'),
    path('metal_structures/', metal_structures, name='metal_structures'),
    path('about_company/', about_company, name='about_company'),
    path('contacts/', contacts, name='contacts'),
    path('cement/', cement, name='cement'),
    path('stone/', stone, name='stone'),
    path('sand/', sand, name='sand'),
    path('vacancies/', vacancies, name='vacancies'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)