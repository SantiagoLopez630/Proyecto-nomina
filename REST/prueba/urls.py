from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
from prueba import views
from rest_framework.documentation import include_docs_urls

router=routers.DefaultRouter()
router.register(r'usuariorest',views.UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('docs/',include_docs_urls(title='doc'))
]