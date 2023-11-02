from django.shortcuts import render
from django.http import JsonResponse

import facturama

# Create your views here.
def obtenerClientes(request):
    facturama._credentials = ('corvusdata', '#corvus1234')
    facturama.sandbox = True
    customers = facturama.Client.all(0)
    return render(request, 'facturas/clientes.html', {'customers': customers })

def capturarCliente(request):
    if request.method == "POST":
        facturama._credentials = ('corvusdata', '#corvus1234')
        facturama.sandbox = True
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
    facturama._credentials = ('corvusdata', '#corvus1234')
    facturama.sandbox = True
    products = facturama.Product.all()
    return render(request, 'facturas/productos.html', {'products': products })


def capturarProducto(request):
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
    facturama._credentials = ('corvusdata', '#corvus1234')
    facturama.sandbox = True
    sucursales = facturama.BranchOffice.all()
    return render(request, 'facturas/sucursales.html', {'sucursales': sucursales })


def capturarSucursal(request):
    if request.method == "POST":
        direccion_sucursal = ["Street","ExteriorNumber","InteriorNumber","Neighborhood","ZipCode","Locality","Municipality","State","Country"]
        branch_office_object = {
            "Name": request.POST.get("Name"),
            "Description": request.POST.get("Description"),
        }
        for clave in direccion_sucursal:
            customer_address[clave] = request.POST.get(clave)

        branch_office_object["Address"] = customer_address
        return JsonResponse(branch_office_object)

def generarCFDI(request):
    data = {
        "Serie": "R",
        "Currency": "MXN",
        "ExpeditionPlace": "78116",
        "PaymentConditions": "CREDITO A SIETE DIAS",
        "Folio": "100",
        "CfdiType": "I",
        "PaymentForm": "03",
        "PaymentMethod": "PUE",
        "Receiver": {
          "Rfc": "RSS2202108U5",
          "Name": "RADIAL SOFTWARE SOLUTIONS",
          "CfdiUse": "P01"
        },
        "Items": [
            {
                "ProductCode": "10101504",
                "IdentificationNumber": "EDL",
                "Description": "Estudios de viabilidad",
                "Unit": "NO APLICA",
                "UnitCode": "MTS",
                "UnitPrice": 50.0,
                "Quantity": 2.0,
                "Subtotal": 100.0,
                "Taxes": [
                    {
                        "Total": 16.0,
                        "Name": "IVA",
                        "Base": 100.0,
                        "Rate": 0.16,
                        "IsRetention": false
                    }
                ],
                "Total": 116.0
            },
            {
                "ProductCode": "10101504",
                "IdentificationNumber": "001",
                "Description": "SERVICIO DE COLOCACION",
                "Unit": "NO APLICA",
                "UnitCode": "E49",
                "UnitPrice": 100.0,
                "Quantity": 15.0,
                "Subtotal": 1500.0,
                "Discount": 0.0,
                "Taxes": [
                    {
                        "Total": 240.0,
                        "Name": "IVA",
                        "Base": 1500.0,
                        "Rate": 0.16,
                        "IsRetention": false
                    }
                ],
                "Total": 1740.0
            }
        ]
    }   