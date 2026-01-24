# Colección global de productos
productos = []

# Opción 1: Sumar 2 números
def sumar():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    print(f"La suma es: {a + b}")

# Opción 2: Crear colección de productos
def crear_productos():
    global productos
    productos = []
    n = int(input("¿Cuántos productos desea registrar?: "))

    for i in range(n):
        print(f"\nProducto {i + 1}")
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        productos.append({"nombre": nombre, "precio": precio})

    print("✅ Productos registrados correctamente")

# Opción 3: Agregar un nuevo producto
def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    productos.append({"nombre": nombre, "precio": precio})
    print("✅ Producto agregado")

# Opción 4: Mostrar producto de precio más bajo
def producto_mas_barato():
    if not productos:
        print("⚠️ No hay productos registrados")
        return

    barato = productos[0]
    for p in productos:
        if p["precio"] < barato["precio"]:
            barato = p

    print("\n🛒 Producto más barato:")
    print(f"Nombre: {barato['nombre']}")
    print(f"Precio: S/. {barato['precio']}")

# Menú principal
def menu():
    while True:
        print("\n===== MENÚ =====")
        print("1. Sumar 2 números")
        print("2. Crear colección de productos")
        print("3. Agregar un nuevo producto")
        print("4. Mostrar el producto de precio más bajo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sumar()
        elif opcion == "2":
            crear_productos()
        elif opcion == "3":
            agregar_producto()
        elif opcion == "4":
            producto_mas_barato()
        elif opcion == "5":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida")

# Ejecutar programa
menu()