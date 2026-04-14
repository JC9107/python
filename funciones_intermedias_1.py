# 1. Actualizar valores en diccionarios y listas
# Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
matriz = [ [10, 15, 20], [3, 7, 14] ]

matriz[1][0]=6
print(matriz)

# Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

cantantes[0]["nombre"]="Enrique Martin Morales"
print(cantantes[0])

# En ciudades, cambia “Cancún” por “Monterrey”
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

ciudades["México"][2]="Monterrey"
print(ciudades["México"])

# En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

coordenadas[0]["latitud"]=9.9355431
print(coordenadas)


# 2. Iterar a través de una lista de diccionarios
# Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente.
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

# Lineas separadas
def iterarDiccionario0(lista):
    for diccionario in lista:
        for llave, valor in diccionario.items():
            print(f"{llave}: {valor}")
        print()

iterarDiccionario0(cantantes)

# Lineas seguidas
def iterarDiccionario1(lista):
    for dic in lista:
        resultado = []
        for llave, valor in dic.items():
            resultado.append(f"{llave} - {valor}")
        print(", ".join(resultado))

iterarDiccionario1(cantantes)


# 3. Obtener valores de una lista de diccionarios
# Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave y una lista de diccionarios. La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista. Por ejemplo, iterarDiccionario2(“nombre”, cantantes).
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

# PRIMERA FORMA
def iterarDiccionario2(llave,lista):
    for i in range(len(lista)):
        resultado=lista[i][llave]
        print(resultado)

iterarDiccionario2("nombre", cantantes)

# SEGUNDA FORMA
def iterarDiccionario3(llave,lista):
    for dicco in lista:
        print(dicco[llave])

iterarDiccionario3("nombre",cantantes)


# 4. Iterar a través de un diccionario con valores de lista
# Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas. La función debe imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave.
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    for llave,valor in diccionario.items():
        print(f"{len(valor)} {llave.upper()}")
        for i in valor:
            print(i)
        print()

imprimirInformacion(costa_rica)
