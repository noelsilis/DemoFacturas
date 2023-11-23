from django.urls import path
from django.urls import re_path as url
from . import views

urlpatterns = [
    path('', views.obtenerClientes, name="clientes"),
    path('new-cliente/', views.capturarCliente, name="new_cliente"),
    path('productos/', views.obtenerProductos, name="productos"),
    path('new-producto/', views.capturarProducto, name="new_producto"),
    path('sucursales/', views.obtenerSucursales, name="sucursales"),
    path('new-sucursal/', views.capturarSucursal, name="new_sucursal"),
    #Ajax
    url(r'^new-client-fact/$', views.catalogs_client, name='new_client_fact'),
    url(r'^new-client-addr/$', views.catalogs_Addr, name='new_client_addr'),
    url(r'^productos/new-product-iva/$', views.catalogs_iva, name='new_product_iva'),
]

