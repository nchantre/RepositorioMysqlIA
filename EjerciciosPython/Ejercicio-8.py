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

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un cliente
    crear_cliente('1234567890', 'Juan', 'Pérez', '555-1234', 'juan@example.com')
    # Leer clientes
    clientes = leer_clientes()
    print(clientes)
