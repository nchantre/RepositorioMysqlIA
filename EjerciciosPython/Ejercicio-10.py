import mysql.connector

# Configuración de la conexión
config = {
    'user': 'root',
    'password': '',  # Cambia esto si tienes contraseña
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'bdventas'
}

def crear_tabla_productos():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS productos (
            idProducto INT AUTO_INCREMENT PRIMARY KEY,
            NombreProducto VARCHAR(255) NOT NULL,
            Cantidad INT NOT NULL
        )
        """
        cursor.execute(query)
        conn.commit()
        print("Tabla 'productos' creada o ya existe.")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")

def crear_producto(nombre, cantidad):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    query = "INSERT INTO productos (NombreProducto, Cantidad) VALUES (%s, %s)"
    cursor.execute(query, (nombre, cantidad))
    conn.commit()
    print("Producto creado correctamente.")
    cursor.close()
    conn.close()

def leer_productos():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    query = "SELECT * FROM productos"
    cursor.execute(query)
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    cursor.close()
    conn.close()

def actualizar_producto(id_producto, nombre, cantidad):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    query = "UPDATE productos SET NombreProducto=%s, Cantidad=%s WHERE idProducto=%s"
    cursor.execute(query, (nombre, cantidad, id_producto))
    conn.commit()
    print("Producto actualizado correctamente.")
    cursor.close()
    conn.close()

def eliminar_producto(id_producto):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    query = "DELETE FROM productos WHERE idProducto=%s"
    cursor.execute(query, (id_producto,))
    conn.commit()
    print("Producto eliminado correctamente.")
    cursor.close()
    conn.close()

def menu():
    while True:
        print("\n--- Menú de Productos ---")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Editar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            crear_producto(nombre, cantidad)
        elif opcion == "2":
            leer_productos()
        elif opcion == "3":
            id_producto = int(input("ID del producto a editar: "))
            nombre = input("Nuevo nombre: ")
            cantidad = int(input("Nueva cantidad: "))
            actualizar_producto(id_producto, nombre, cantidad)
        elif opcion == "4":
            id_producto = int(input("ID del producto a eliminar: "))
            eliminar_producto(id_producto)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Descomenta estas líneas para crear la tabla y mostrar el menú
crear_tabla_productos()
menu()