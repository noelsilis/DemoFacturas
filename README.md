# DemoFacturas
Esta app de django es una demo inicial para consumir la API de Facturama mediante el SDK de Python

## 1. Ambientación dev

### 1.1 Prerrequisitos

- Python 3.10
- pip
- pipenv

### 1.2 Crear entorno virtual
- 1.2.1 Clona el proyecto.

- 1.2.2 Dentro de la carpeta del proyecto **DemoFacturas** inicializa el entorno virtual:
```
pipenv shell
```

### 1.3 Instala los paquetes pip necesarios
- 1.3.1 Instala los paquetes especifcados desde el archivo **requirements.txt**:
```
pip install -r requirements.txt
```

## 2. Documentación oficial de API Facturama

- 2.2 Guia de inicio https://apisandbox.facturama.mx/guias
- 2.3 Guia basica de uso https://apisandbox.facturama.mx/Docs
- 2.4 Repositorio https://github.com/Facturama/facturama-python-sdk

## 3. Pasos para utilizar Facturama

### 3.1 Crear una cuenta en el entorno de pruebas de Facturama

- 3.1.1 El entorno de pruebas de facturama es sandbox https://dev.facturama.mx/api/login

### 3.2 Descargar los sellos digitales para pruebas

- 3.2.1 Sellos/Certificados digitales https://apisandbox.facturama.mx/guias/conocimientos/sellos-digitales-pruebas

### 3.3 Configurar cuenta sandbox con información de algun sello digital

- 3.3.1 Configurar perfil
- 3.3.2 Configurar catalogos de productos y clientes

### 3.4 Configurar app django

- 3.4.1 Ajustar las credenciales de Facturama en django.
