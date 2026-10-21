def calcular_recibo():
    print("=" * 50)
    print("         SISTEMA DE RECIBO DE COMPRA INTERACTIVO")
    print("=" * 50)
    
    productos = []
    
    # Bucle principal para capturar múltiples productos
    while True:
        nombre = input("\nIngrese el nombre del producto (o escriba 'salir' para terminar): ").strip()
        
        # Condición de salida
        if nombre.lower() == 'salir':
            if not productos:
                print("⚠️ No se han registrado productos. ¡Programa finalizado!")
                return
            break
        
        # Validación de que el nombre no esté vacío
        if not nombre:
            print("⚠️ El nombre del producto no puede estar vacío. Intente de nuevo.")
            continue
        
        # Validación del precio (conversión de tipos y manejo de errores)
        while True:
            try:
                precio = float(input(f"Ingrese el precio unitario de '{nombre}': $"))
                if precio <= 0:
                    print("⚠️ El precio debe ser mayor a cero.")
                    continue
                break
            except ValueError:
                print("⚠️ Entrada inválida. Por favor, ingrese un número válido para el precio.")
        
        # Validación de la cantidad
        while True:
            try:
                cantidad = int(input(f"Ingrese la cantidad de '{nombre}': "))
                if cantidad <= 0:
                    print("⚠️ La cantidad debe ser un número entero mayor a cero.")
                    continue
                break
            except ValueError:
                print("⚠️ Entrada inválida. Por favor, ingrese un número entero válido.")
        
        # Cálculo del subtotal del producto usando operadores aritméticos
        subtotal_producto = precio * cantidad
        
        # Guardamos la información en una estructura (diccionario) dentro de una lista
        productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
            "subtotal": subtotal_producto
        })
        
        print(f"✅ ¡Producto agregado! Subtotal: ${subtotal_producto:.2f}")

    # Cálculos finales de la compra
    subtotal_general = sum(p["subtotal"] for p in productos)
    iva = subtotal_general * 0.16  # Impuesto del 16% (IVA estándar)
    total = subtotal_general + iva

    # Mostrando el recibo final claramente formateado
    print("\n" + "=" * 60)
    print("                      TICKET DE COMPRA")
    print("=" * 60)
    print(f"{'PRODUCTO':<22} {'CANT':<6} {'PRECIO':<10} {'SUBTOTAL':<10}")
    print("-" * 60)
    
    # Recorremos la lista para imprimir cada producto alineado
    for p in productos:
        print(f"{p['nombre']:<22} {p['cantidad']:<6} ${p['precio']:<9.2f} ${p['subtotal']:<9.2f}")
        
    print("-" * 60)
    print(f"{'Subtotal:':<39} ${subtotal_general:>10.2f}")
    print(f"{'IVA (16%):':<39} ${iva:>10.2f}")
    print(f"{'TOTAL A PAGAR:':<39} ${total:>10.2f}")
    print("=" * 60)
    print("                ¡Gracias por su compra!")
    print("=" * 60)

# Punto de entrada del programa
if __name__ == "__main__":
    calcular_recibo()
    