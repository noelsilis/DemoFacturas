async function obtenerCliente(url) {
    try {
        const clientes = await obtenerDatos(url);
        const id_cliente = '';
        cargarClientes(clientes, id_cliente);
    } catch (error) {
        console.error(error);
    }
}

async function obtenerFormaPago(url) {
    try {
        const formas = await obtenerDatos(url);
        const id_forma = '';
        cargarFormaPago(formas, id_forma);
    } catch (error) {
        console.error(error);
    }
}

async function obtenerProducto(url) {
    try {
        const productos = await obtenerDatos(url);
        const id_producto = '';
        cargarProductos(productos, id_producto);
    } catch (error) {
        console.error(error);
    }
}

async function listarProductos(url) {
    try {
        const productos = await obtenerDatos(url);
        listarProducto(productos);
    } catch (error) {
        console.error(error);
    }
}

async function obtenerUso(url) {
    try {
        const usos = await obtenerDatos(url);
        const id_uso = '';
        cargarUso(usos, id_uso);
    } catch (error) {
        console.error(error);
    }
}

async function obtenerMetodo(url) {
    try {
        const metodos = await obtenerDatos(url);
        const id_metodo = '';
        cargarMetodos(metodos, id_metodo);
    } catch (error) {
        console.error(error);
    }
}

async function obtenerDatos(url) {
    //console.log(url);
    return fetch(url)
        .then((res) => {
            if (res.status === 200) {
                return res.json();
            } else {
                // Manejar errores aquí, por ejemplo, lanzar una excepción
                throw new Error(`Error en la solicitud: ${res.status}`);
            }
        })
        .then((data) => {

            console.log(data);
            return data && data['data'];
        })
        .catch((error) => {
            console.error(error);
            // Retornar un valor predeterminado o manejar el error de otra manera si es necesario
            return null;
        });
}

function cargarClientes(lista, id) {
    const clienteSelect = document.getElementById("id_select_cliente");
    if (id == '') {
        clienteSelect.innerHTML = `<option selected="">Choose a Client</option>`;
    }
    for (index in lista) {
        let cliente = lista[index];
        if (cliente.id_cliente == id) {
            clienteSelect.innerHTML = `<option selected="">${cliente.nombre}</option>`;
        } else {
            const option = document.createElement("option");
            option.value = cliente.id_cliente;
            option.textContent = cliente.nombre;
            clienteSelect.appendChild(option);
        }
    }
}

function cargarFormaPago(lista, id) {
    const formaSelect = document.getElementById("id_select_forma_pago");
    if (id == '') {
        formaSelect.innerHTML = `<option selected="">Choose a Payment Form</option>`;
    }
    for (index in lista) {
        let forma = lista[index];
        if (forma.id_forma == id) {
            formaSelect.innerHTML = `<option selected="">${forma.id_forma+" "+forma.nombre}</option>`;
        } else {
            const option = document.createElement("option");
            option.value = forma.id_forma;
            option.textContent = forma.id_forma + " - " + forma.nombre;
            formaSelect.appendChild(option);
        }
    }
}

function cargarProductos(lista, id) {
    const productoSelect = document.getElementById("id_select_producto");
    if (id == '') {
        productoSelect.innerHTML = `<option selected="">Choose a Product</option>`;
    }
    for (index in lista) {
        let producto = lista[index];
        if (producto.Id == id) {
            productoSelect.innerHTML = `<option selected="">${producto.Name}</option>`;
        } else {
            const option = document.createElement("option");
            option.value = producto.Id;
            option.textContent = producto.Name;
            productoSelect.appendChild(option);
        }
    }
}

function listarProducto(lista) {
    const table = document.getElementById("id_tbody");
    const id_product = document.getElementById("id_select_producto").value;
    lista.forEach((producto) => {
        //Filtrar el producto que contenga el ID seleccionado
        if (id_product == producto['Id']) {
            console.log(producto);
            //Crear un nuevo renglon de la tabla
            let tr = document.createElement("tr");
            // console.log(item['Id'] + "HOLAAAAA");

            //INTENTAR HACER DESESTRUCTURACION PARA OBTENER SOLO LOS DATOS QUE SE REQUIEREN MOSTRAR
            let {
                UnitCode,
                Description,
                Price,
                Taxes: {
                    0: {
                        Rate
                    }
                }
            } = producto;
            const Quantity = 1;
            let Subtotal = Price;
            let Discount = 0;
            let Total = Price + (Price * Rate);
            let valores = { Quantity, UnitCode, Description, Price, Subtotal, Discount, Rate, Total };
            console.log(valores);
            //FIN DESESTRUCTURACION

            // Traer los valores del producto
            let valor = Object.values(valores);
            //Para cada valor asignarle una posicion en las columnas
            valor.forEach((val) => {

                let td = document.createElement("td");
                td.innerText = val; // Asignar valor
                tr.appendChild(td); // Agregar la celda a la tabla
            })

            table.appendChild(tr); // Agregar la columna a la tabla
        }

    });
}

function crearTabla(valor) {
    let td = document.createElement("td");
    td.innerText = val; // Asignar valor
    tr.appendChild(td);

}

function cargarUso(lista, id) {
    const usoSelect = document.getElementById("id_select_cfdi_use");
    if (id == '') {
        usoSelect.innerHTML = `<option selected="">Choose a Use</option>`;
    }
    for (index in lista) {
        let uso = lista[index];
        if (uso.id_uso == id) {
            usoSelect.innerHTML = `<option selected="">${uso.nombre}</option>`;
        } else {
            const option = document.createElement("option");
            option.value = uso.id_uso;
            option.textContent = uso.id_uso + " - " + uso.nombre;
            usoSelect.appendChild(option);
        }
    }
}

function cargarMetodos(lista, id) {
    const metodoSelect = document.getElementById("id_select_metodo_pago");
    if (id == '') {
        metodoSelect.innerHTML = `<option selected="">Choose a Payment Method</option>`;
    }
    for (index in lista) {
        let metodo = lista[index];
        if (metodo.id_metodo == id) {
            metodoSelect.innerHTML = `<option selected="">${metodo.nombre}</option>`;
        } else {
            const option = document.createElement("option");
            option.value = metodo.id_metodo;
            option.textContent = metodo.id_metodo + " - " + metodo.nombre;
            metodoSelect.appendChild(option);
        }
    }
}