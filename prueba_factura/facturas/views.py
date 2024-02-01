from django.shortcuts import render
from django.http import JsonResponse
from decouple import config

import facturama

# Create your views here.
def obtenerClientes(request):
    user = config('FACTURAMA_USER')
    facturama._credentials = (config('FACTURAMA_USER'), config('FACTURAMA_PASSWORD'))
    facturama.sandbox = False
    facturama.api_lite = True
    customers = facturama.Client.all(0)
    print("\n\nUsuario: " + user + "\n\n")
    return render(request, 'facturas/clientes.html', {'customers': customers })

def capturarCliente(request):
    user = config('FACTURAMA_USER')
    if request.method == "POST":
        facturama._credentials =(config('FACTURAMA_USER'), config('FACTURAMA_PASSWORD'))
        facturama.sandbox = config('FACTURAMA_SANDBOX')
        datos_cliente = ["Rfc","Name","FiscalRegime","Email","CfdiUse","TaxResidence","NumRegIdTrib","TaxZipCode"]
        direccion_cliente = ["Street","ExteriorNumber","InteriorNumber","Neighborhood","ZipCode","Locality","Municipality","State","Country"]
        customer_object = {}
        customer_address = {}
        customer["Id"] = ""
        for clave in datos_cliente:
            customer_object[clave] = request.POST.get(clave)

        for clave in direccion_cliente:
            customer_address[clave] = request.POST.get(clave)
        
        customer_object["Address"] = customer_address
        facturama.Client.create(customer_object)
        return render(request, 'facturas/clientes.html')

def obtenerProductos(request):
    user = config('FACTURAMA_USER')
    print("Passowrd",config('FACTURAMA_PASSWORD'))
    facturama._credentials =(config('FACTURAMA_USER'), config('FACTURAMA_PASSWORD'))
    facturama.sandbox = config('FACTURAMA_SANDBOX')
    products = facturama.Product.all()
    return render(request, 'facturas/productos.html', {'products': products })


def capturarProducto(request):
    user = config('FACTURAMA_USER')
    if request.method == "POST":
        datos_producto = ["Unit","UnitCode","IdentificationNumber","Name","Description","Price","CodeProdServ","CuentaPredial"]
        impuesto = ["Name","Rate","IsRetention","IsFederalTax"]
        product_object = {}
        taxes = {}
        for clave in datos_producto:
            product_object[clave] = request.POST.get(clave)

        for clave in impuesto:
            taxes[clave] = request.POST.get(clave)

        product_object["Taxes"] = taxes
        return JsonResponse(product_object)


def obtenerSucursales(request):
    facturama._credentials =(config('FACTURAMA_USER'), config('FACTURAMA_PASSWORD'))
    facturama.sandbox = config('FACTURAMA_SANDBOX')
    sucursales = facturama.BranchOffice.all()
    return render(request, 'facturas/sucursales.html', {'sucursales': sucursales })


# def capturarSucursal(request):
#     user = config('FACTURAMA_USER')
#     if request.method == "POST":
#         direccion_sucursal = ["Street","ExteriorNumber","InteriorNumber","Neighborhood","ZipCode","Locality","Municipality","State","Country"]
        
#         branch_office_object = {
            
#             "Name": request.POST.get("Name"),
#             "Description": request.POST.get("Description"),
#         }
#         for clave in direccion_sucursal:
#             customer_address[clave] = request.POST.get(clave)

#         branch_office_object["Address"] = customer_address
#         return JsonResponse(branch_office_object)

# def generarCFDI(request):
#     user = config('FACTURAMA_USER')

#     data = {
#         "Serie": "R",
#         "Currency": "MXN",
#         "ExpeditionPlace": "78116",
#         "PaymentConditions": "CREDITO A SIETE DIAS",
#         "Folio": "100",
#         "CfdiType": "I",
#         "PaymentForm": "03",
#         "PaymentMethod": "PUE",
#         "Receiver": {
#           "Rfc": customer.Rfc,
#           "Name": customer.Name,
#           "CfdiUse": "P01"
#         },
#         "Items": [
#             {
#                 "ProductCode": "10101504",
#                 "IdentificationNumber": "EDL",
#                 "Description": "Estudios de viabilidad",
#                 "Unit": "NO APLICA",
#                 "UnitCode": "MTS",
#                 "UnitPrice": 50.0,
#                 "Quantity": 2.0,
#                 "Subtotal": 100.0,
#                 "Taxes": [
#                     {
#                         "Total": 16.0,
#                         "Name": "IVA",
#                         "Base": 100.0,
#                         "Rate": 0.16,
#                         "IsRetention": False
#                     }
#                 ],
#                 "Total": 116.0
#             },
#             {
#                 "ProductCode": "10101504",
#                 "IdentificationNumber": "001",
#                 "Description": "SERVICIO DE COLOCACION",
#                 "Unit": "NO APLICA",
#                 "UnitCode": "E49",
#                 "UnitPrice": 100.0,
#                 "Quantity": 15.0,
#                 "Subtotal": 1500.0,
#                 "Discount": 0.0,
#                 "Taxes": [
#                     {
#                         "Total": 240.0,
#                         "Name": "IVA",
#                         "Base": 1500.0,
#                         "Rate": 0.16,
#                         "IsRetention": False
#                     }
#                 ],
#                 "Total": 1740.0
#             }
#         ]
#     }   