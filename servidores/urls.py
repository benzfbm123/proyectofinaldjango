from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('servidores/', views.lista_servidores, name='lista_servidores'),
    path('servidores/<int:pk>/', views.detalle_servidor, name='detalle_servidor'),
    path('servidores/crear/', views.crear_servidor, name='crear_servidor'),
    path('servidores/<int:pk>/editar/', views.editar_servidor, name='editar_servidor'),
    path('servidores/<int:pk>/eliminar/', views.eliminar_servidor, name='eliminar_servidor'),
]