import mysql.connector

# Cadena de conexión
config = {
    'user': 'root',
    'password': '',  # Cambia esto si tienes contraseña
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'bdventas'
}

def conectar():
    return mysql.connector.connect(**config)

# CRUD para la tabla Clientes

def crear_cliente(cedula, nombre, apellidos, telefono, email):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
        INSERT INTO Clientes (CedulaCliente, NombreCliente, ApellidosCliente, TelefonoCliente, EmailCliente)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (cedula, nombre, apellidos, telefono, email))
    conn.commit()
    cursor.close()
    conn.close()

def leer_clientes():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Clientes")
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados

def actualizar_cliente(id_cliente, cedula, nombre, apellidos, telefono, email):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
        UPDATE Clientes
        SET CedulaCliente=%s, NombreCliente=%s, ApellidosCliente=%s, TelefonoCliente=%s, EmailCliente=%s
        WHERE IdCliente=%s
    """
    cursor.execute(sql, (cedula, nombre, apellidos, telefono, email, id_cliente))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_cliente(id_cliente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Clientes WHERE IdCliente=%s", (id_cliente,))
    conn.commit()
    cursor.close()
    conn.close()

def menu():
    while True:
        print("\n--- Menú de Clientes ---")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Editar cliente")
        print("4. Eliminar cliente")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            apellidos = input("Apellidos: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            crear_cliente(cedula, nombre, apellidos, telefono, email)
            print("Cliente registrado correctamente.")
        elif opcion == "2":
            clientes = leer_clientes()
            if clientes:
                for c in clientes:
                    print(f"ID: {c['IdCliente']}, Cédula: {c['CedulaCliente']}, Nombre: {c['NombreCliente']} {c['ApellidosCliente']}, Teléfono: {c['TelefonoCliente']}, Email: {c['EmailCliente']}")
            else:
                print("No hay clientes registrados.")
        elif opcion == "3":
            clientes = leer_clientes()
            if not clientes:
                print("No hay clientes para editar.")
                continue
            for c in clientes:
                print(f"ID: {c['IdCliente']}, Nombre: {c['NombreCliente']} {c['ApellidosCliente']}")
            id_cliente = input("Ingrese el ID del cliente a editar: ")
            cedula = input("Nueva Cédula: ")
            nombre = input("Nuevo Nombre: ")
            apellidos = input("Nuevos Apellidos: ")
            telefono = input("Nuevo Teléfono: ")
            email = input("Nuevo Email: ")
            actualizar_cliente(id_cliente, cedula, nombre, apellidos, telefono, email)
            print("Cliente actualizado correctamente.")
        elif opcion == "4":
            clientes = leer_clientes()
            if not clientes:
                print("No hay clientes para eliminar.")
                continue
            for c in clientes:
                print(f"ID: {c['IdCliente']}, Nombre: {c['NombreCliente']} {c['ApellidosCliente']}")
            id_cliente = input("Ingrese el ID del cliente a eliminar: ")
            eliminar_cliente(id_cliente)
            print("Cliente eliminado correctamente.")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()