from django.urls import path
from . import views

urlpatterns = [
    path('', views.obtenerClientes, name="clientes"),  
    path('new-cliente/', views.capturarCliente, name="new_cliente"), 
    path('productos/', views.obtenerProductos, name="productos"),
    path('new-producto/', views.capturarProducto, name="new_producto"),
    path('sucursales/', views.obtenerSucursales, name="sucursales"), 
]

