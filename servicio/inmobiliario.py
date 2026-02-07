def menu_inmobiliario():
    while True:
        print("\n--- SISTEMA INMOBILIARIO ---")
        print("1. Registrar inmueble")
        print("2. Listar inmuebles")
        print("3. Volver")

        opcion = input("Seleccione opcion: ")

        if opcion == "1":
            registrar_inmueble()
        elif opcion == "2":
            listar_inmuebles()
        elif opcion == "3":
            break
        else:
            print("Opcion incorrecta")

def registrar_inmueble():
    tipo = input("Tipo de inmueble: ")
    direccion = input("Direccion: ")
    precio = input("Precio: ")

    print("Inmueble registrado ✔")
    print(tipo, direccion, precio)

def listar_inmuebles():
    print("Listado de inmuebles (ejemplo)")