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

    #Factura
    path('new-sucursal/', views.capturarSucursal, name="new_sucursal"),
    path('get-clients/', views.obtenerCliente, name="get_clients"),
    path('facturas/', views.listarCFDI, name="facturas"),
    path('cfdi/', views.cfdi_get, name="get_cfdi"),
    path('get-products/', views.obtenerProducto, name="get_product"),
    path('get-forms/', views.obtenerForma, name="get_payment_form"),
    path('get-usos-cfdi/', views.obtenerUsoCFDI, name="get_cfdi_use"),
    path('metodos', views.obtenerMetodo, name="get_payment_method"),
]

