from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from nomina import views as empleados_views 

# Definir el router para las vistas de empleados
router = routers.DefaultRouter()
router.register(r'empleados', empleados_views.EmpleadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='API Documentation')),
    path('', empleados_views.home, name='home'),
    path('empleados/', empleados_views.empleadolist, name='empleadolist'),
    path('empleados/crear/', empleados_views.crearEmpleado, name='crearEmpleado'),
    path('empleados/<int:id_empleado>/seguridad_social/', empleados_views.seguridad_social1, name='seguridad_social1'),
    path('empleados/<int:id_empleado>/', empleados_views.detalle_empleado, name='detalle_empleado'),
    path('cesantias/calculator/', empleados_views.cesantias_calculator, name='cesantias_calculator'),
    path('empleados/<int:id_empleado>/cesantias/', empleados_views.detalle_cesantias, name='detalle_cesantias'),
]
