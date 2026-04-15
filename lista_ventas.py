# 1. Carga de Datos:
ventas=[
    {"fecha": "2025-05-15", "producto": "Papel higiénico", "cantidad": "5", "precio": "7.70"},
    {"fecha": "2025-06-01", "producto": "Pollo entero", "cantidad": "8", "precio": "9.40"},
    {"fecha": "2025-04-30", "producto": "Galletas Ritz", "cantidad": "6", "precio": "2.00"},
    {"fecha": "2025-06-23", "producto": "Pollo entero", "cantidad": "4", "precio": "11.70"},
    {"fecha": "2025-04-30", "producto": "Agua San Mateo", "cantidad": "11", "precio": "2.40"}
]

# 2. Calculo de Ingresos Totales:
# Considere ingresos totales como uno solo, ya que al llamarse mi lista "ventas" y pedirme los ingresos totales de ventas, en caso fuera cada venta, se operaria de forma similar a esta:
"""
for dic in ventas:
    precio = float(dic["precio"])
    cantidad = float(dic["cantidad"])

    dic["Ingreso Total"] = precio*cantidad

print(ventas)
"""

resultado=0
for dic in ventas:
    resultado = resultado + float(dic["cantidad"]) * float(dic["precio"])

print(resultado)

#3. Analisis del Producto Mas Vendido:
ventas_por_producto={}
for dico in ventas:
    producto = dico["producto"]
    cantidad = float(dico["cantidad"])

    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

mas_vendido = ""
mayor_cantidad = 0

for producto, cantidad in ventas_por_producto.items():
    if cantidad > mayor_cantidad:
        mayor_cantidad = cantidad
        mas_vendido = producto

print(mas_vendido)

#4. Promedio de Precio por Producto:
precios_por_producto={}
for diccio in ventas:
    producto = diccio["producto"]
    suma = float(diccio["cantidad"]) * float(diccio["precio"])
    cantidad = float(diccio["cantidad"])

    if producto in precios_por_producto:
        precios_por_producto[producto] = (
            precios_por_producto[producto][0] + suma,
            precios_por_producto[producto][1] + cantidad
            )
    else:
        precios_por_producto[producto] = (suma, cantidad)

print(precios_por_producto)

for producto, tupla in precios_por_producto.items():
    promedio = tupla[0]/tupla[1]
    print(f"{producto}: {round(promedio,2)}")

# 5. Ventas por Dia:
ingresos_por_dia={}

for dicco in ventas:
    fecha = dicco["fecha"]
    ingreso = float(dicco["cantidad"]) * float(dicco["precio"])

    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

print(ingresos_por_dia)

# 6. Representación de Datos:
resumen_ventas={}

for ventap in ventas:
    product = ventap["producto"]
    cant = float(ventap["cantidad"])
    ingresot = float(ventap["cantidad"]) * float(ventap["precio"])

    if product in resumen_ventas:
        resumen_ventas[product] = {
            "Cantidad": resumen_ventas[product]["Cantidad"] + cant,
            "Ingreso Total": resumen_ventas[product]["Ingreso Total"] + ingresot,
        }
    else:
        resumen_ventas[product] = {"Cantidad": cant, "Ingreso Total": ingresot}

for prod, val in resumen_ventas.items():
    prom = val["Ingreso Total"]/val["Cantidad"]
    val["Promedio"] = round(prom,2)

print(resumen_ventas)
