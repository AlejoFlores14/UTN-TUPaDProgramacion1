"""Pido el nombre del cliente y la cantidad de productos"""
"""Uso isalpha para validar que el nombre ingresado solo contenga letras y no este vacio"""
nombre = input("Ingrese su nombre: ")
while not nombre.isalpha() or nombre == "":
    print("Error: El nombre debe contener solo letras y no estar vacío.")
    nombre = input("Ingrese su nombre: ")
"""Uso isdigit para validar que la cantidad de productos sea un numero entero mayor a 0"""
cantidadUno = input("Ingrese una cantidad: ")
while not cantidadUno.isdigit() or int(cantidadUno) <= 0:
    print("Error: Ingrese un número entero mayor a 0.")
    cantidadUno = input("Ingrese una cantidad: ")
cantidad = int(cantidadUno)

"""Inicializo variables en 0"""
precioSinDescuento = 0
precioConDescuento = 0
precioproducto = []

"""precio del producto y si tiene descuento """
for i in range(1, cantidad + 1):
    precioUno = input(f"Ingrese el precio del producto {i}: ")
    while not precioUno.isdigit():
        print("Error: El precio debe ser un número entero.")
        precioUno = input(f"Ingrese el precio del producto {i}: ")
    precio = int(precioUno)
    """Pregunto si el producto tiene descuento y luego valido la respuesta """
    descuento = input(f"¿El producto {i} tiene descuento? (S/N): ").lower()
    while descuento not in ['s', 'n']:
        print("Error: Ingrese 's' para sí o 'n' para no.")
        descuento = input(f"¿El producto {i} tiene descuento? (S/N): ").lower()


    precioSinDescuento += precio
    """ aplico el descuento en caso de tener """
    if descuento == "s":
        valorFinal = precio * 0.90
    else:
        valorFinal = float(precio)

    precioConDescuento += valorFinal
    precioproducto.append(valorFinal)
"""Calculo el ahorro total y el promedio con descuento"""
ahorroTotal = precioSinDescuento - precioConDescuento
promedio = precioConDescuento / cantidad
"""muestro los resultados al cliente"""
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")
for i in range(cantidad):
    print(f"Producto {i+1} - Precio: {precioproducto[i]}")
print(f"Total sin descuento: {precioSinDescuento}")
print(f"Total con descuento: {precioConDescuento}")
print(f"Ahorro total: {ahorroTotal}")
print(f"Promedio con descuento: {promedio}")
