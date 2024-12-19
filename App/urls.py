from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_products, name='lista_productos'),
    path('crear_producto/', views.crear_product, name='crear_producto'),
    path('editar_Producto/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar_Producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]
