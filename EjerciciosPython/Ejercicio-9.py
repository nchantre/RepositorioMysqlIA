import cx_Oracle

# Configuración de la cadena de conexión
username = 'tu_usuario'
password = 'tu_contraseña'
dsn = 'localhost/orclpdb1'  # Cambia según tu configuración

def get_connection():
    return cx_Oracle.connect(username, password, dsn)

# CREATE
def insertar_persona(nombre, edad):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO personas (nombre, edad) VALUES (:1, :2)", (nombre, edad))
    conn.commit()
    cursor.close()
    conn.close()

# READ
def obtener_personas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, edad FROM personas")
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados

# UPDATE
def actualizar_persona(id_persona, nuevo_nombre, nueva_edad):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE personas SET nombre=:1, edad=:2 WHERE id=:3", (nuevo_nombre, nueva_edad, id_persona))
    conn.commit()
    cursor.close()
    conn.close()

# DELETE
def eliminar_persona(id_persona):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM personas WHERE id=:1", (id_persona,))
    conn.commit()
    cursor.close()
    conn.close()

# Ejemplo de uso
if __name__ == "__main__":
    # insertar_persona('Juan', 30)
    # print(obtener_personas())
    # actualizar_persona(1, 'Juan Actualizado', 31)
    # eliminar_persona(1)
    pass