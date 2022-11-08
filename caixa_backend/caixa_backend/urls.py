from django.urls import path,include
from django.contrib import admin

from rest_framework import routers

from api_constuctor.api import viewsets as itemsviewset

route = routers.DefaultRouter()

route.register('itens', itemsviewset.ItemViewSet, basename="Itens")

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(route.urls)),
    path('api-auth/', include('rest_framework.urls')),
]