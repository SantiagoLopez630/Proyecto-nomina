from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from prueba import views as prueba_views
from nomina import views as nomina_views
from rest_framework.documentation import include_docs_urls

# Definir routers para las vistas de cada aplicación si es necesario
router_prueba = routers.DefaultRouter()
router_prueba.register(r'usuariosrest', prueba_views.UsuarioViewSet) 

router_nomina = routers.DefaultRouter()
router_nomina.register(r'empleados', nomina_views.EmpleadoViewSet)  

urlpatterns = [
    path('', include(router_prueba.urls)),  
    path('', include(router_nomina.urls)),  
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='API Documentation')), 
]

