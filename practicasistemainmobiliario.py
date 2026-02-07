import sqlite3
from servicio.inmobiliario import menu_inmobiliario
from email import enviar_email

DB = "sistema.db"

def conectar():
    return sqlite3.connect(DB)

def crear_tabla_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT,
            correo TEXT
        )
    """)
    conn.commit()
    conn.close()

def agregar_usuario():
    usuario = input("Ingrese usuario: ")
    correo = input("Ingrese correo: ")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO usuarios (usuario, correo) VALUES (?, ?)",
        (usuario, correo)
    )
    conn.commit()
    conn.close()

    print("Usuario agregado correctamente ✔")

    subject = "Registro exitoso"
    mensaje = f"Hola {usuario}, tu usuario fue registrado correctamente."
    enviar_email(correo, subject, mensaje)

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Agregar usuario")
        print("2. Sistema inmobiliario")
        print("3. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            menu_inmobiliario()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    crear_tabla_usuarios()
    menu()