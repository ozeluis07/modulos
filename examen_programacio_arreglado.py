import os


def main():
    mensaje = "¡Bienvenido a la Tienda Vale Todo!"
    nombre = leer_nombre(mensaje)

    os.system("cls")
    precio_minimo = float(input("Digite el precio mínimo: "))
    porcentaje = float(input("Digite el porcentaje de descuento: "))

    subtotal_acumulado = 0.0
    descuento_acumulado = 0.0
    iva_acumulado = 0.0
    total_acumulado = 0.0
    contador = 0

    agregar_otro = "s"
    while agregar_otro == "s":
        contador += 1
        print(f"--- Producto #{contador} ---")
        precio = float(input("Digite el precio del artículo: "))
        cantidad = int(input("¿Cuántas unidades va a comprar?: "))

        subtotal_acumulado, subtotal, cumple = calcular_total_productos(
            precio, cantidad, precio_minimo, subtotal_acumulado
        )

        if cumple:
            total, subtotal, descuento, iva = calcular_total(subtotal, porcentaje, 0.15)
            mostrar_factura_producto(contador, precio, cantidad, subtotal, porcentaje, descuento, iva, total)

            descuento_acumulado += descuento
            iva_acumulado += iva
            total_acumulado += total

        print("=" * 50)
        os.system("PAUSE")
        agregar_otro = input("¿Desea agregar otro producto? (s/n): ").strip().lower()

    mostrar_factura(nombre, subtotal_acumulado, porcentaje, total_acumulado, subtotal_acumulado, descuento_acumulado, iva_acumulado)


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


def calcular_total_productos(precio, cantidad, precio_minimo, subtotal_acumulado):
    # Calcula el subtotal del producto actual (antes de aplicar descuento)
    subtotal = calcular_subtotal(precio, cantidad)

    # Solo acumula si el precio supera el precio mínimo establecido
    if precio >= precio_minimo:
        subtotal_acumulado += subtotal
        print(f"Producto válido -> Precio: {precio:.2f} | Cantidad: {cantidad} | Subtotal: {subtotal:.2f}")
        return subtotal_acumulado, subtotal, True
    else:
        print(f"Producto NO cumple el precio mínimo (Precio: {precio:.2f}), no se acumula.")
        return subtotal_acumulado, subtotal, False


def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_descuento(subtotal, porcentaje):
    return subtotal * (porcentaje / 100)


def mostrar_factura_producto(numero, precio, cantidad, subtotal, porcentaje, descuento, iva, total):
    print("-" * 40)
    print(f"Factura del producto #{numero}")
    print(f"Precio unitario: {precio:.2f}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Descuento ({porcentaje}%): {descuento:.2f}")
    print(f"IVA: {iva:.2f}")
    print(f"Total del producto: {total:.2f}")
    print("-" * 40)


def mostrar_factura(nombre, subtotal_total, porcentaje, total, subtotal, descuento, iva):
    print("*" * 40)
    print("FACTURA GENERAL")
    print(f"Cliente: {nombre}")
    print(f"Subtotal acumulado: {subtotal_total:.2f}")
    print(f"Porcentaje de descuento: {porcentaje}%")
    print(f"Descuento acumulado: {descuento:.2f}")
    print(f"IVA: {iva:.2f}")
    print(f"Total: {total:.2f}")
    print("*" * 40)


if __name__ == "__main__":
    main()