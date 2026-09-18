import os


def main():
    mensaje = "¡Bienvenido a la Tienda Vale Todo!"
    nombre = leer_nombre(mensaje)

    os.system("cls")
    numero_productos = int(input("Digite el número de productos a comprar: "))
    precio_minimo = float(input("Digite el precio mínimo: "))
    porcentaje = float(input("Digite el porcentaje de descuento: "))

    productos = []
    for i in range(numero_productos):
        precio = float(input("Digite el precio del artículo: "))
        cantidad = int(input("¿Cuántas unidades va a comprar?: "))
        productos.append((precio, cantidad))
        os.system("PAUSE")
        print("="*50)

    subtotal_total = calcular_total_productos(productos, precio_minimo)
    total, subtotal, descuento_total, iva = calcular_total(subtotal_total, porcentaje, 0.15)
    mostrar_factura(nombre, subtotal_total, porcentaje, total, subtotal, descuento_total, iva)


def leer_nombre(mensaje):
    os.system("cls")
    print(mensaje)
    print("*" * 20)
    return input("Digite el nombre del cliente: ")


def calcular_total(subtotal, porcentaje, impuesto):
    descuento_total = calcular_descuento(subtotal, porcentaje)
    iva = (subtotal - descuento_total) * impuesto
    total = subtotal - descuento_total + iva
    return total, subtotal, descuento_total, iva


def calcular_total_productos(productos, precio_minimo):
    subtotal_total = 0.0
    print("-" * 40)
    print("Productos que cumplen el precio mínimo:")
    for precio, cantidad in productos:
        if precio >= precio_minimo:
            subtotal = calcular_subtotal(precio, cantidad)
            subtotal_total += subtotal
            print(f"  Precio: {precio:.2f} | Cantidad: {cantidad} | Subtotal: {subtotal:.2f}")
    print("-" * 40)
    return subtotal_total


def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_descuento(subtotal, porcentaje):
    return subtotal * (porcentaje / 100)


def mostrar_factura(nombre, subtotal_total, porcentaje, total, subtotal, descuento, iva):
    print("*" * 40)
    print(f"Cliente: {nombre}")
    print(f"Subtotal acumulado: {subtotal_total:.2f}")
    print(f"Porcentaje de descuento: {porcentaje}%")
    print(f"Descuento acumulado: {descuento:.2f}")
    print(f"IVA: {iva:.2f}")
    print(f"Total: {total:.2f}")
    print("*" * 40)


if __name__ == "__main__":
    main()