import oracledb

def conectar():
    try:
        conn = oracledb.connect(
            user="PRODUCTO",
            password="Root123",
            dsn="localhost:1521/FREEPDB1"
        )
        return conn
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None

def registrar_genero(conn):
    nombre = input("Ingrese el nombre del género: ")
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO GENERO (ID_GENERO, NOMBRE_GENERO) VALUES (GENERO_SEQ.NEXTVAL, :1)",
                [nombre]
            )
        conn.commit()
        print("Género registrado exitosamente.")
    except Exception as e:
        print("Error al registrar género:", e)

def listar_generos(conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT ID_GENERO, NOMBRE_GENERO FROM GENERO")
            rows = cursor.fetchall()
            print("\nListado de Géneros:")
            for row in rows:
                print(f"ID: {row[0]}, Nombre: {row[1]}")
    except Exception as e:
        print("Error al listar géneros:", e)

def actualizar_genero(conn):
    try:
        id_genero = int(input("Ingrese el ID del género a actualizar: "))
        nuevo_nombre = input("Ingrese el nuevo nombre del género: ")
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE GENERO SET NOMBRE_GENERO = :1 WHERE ID_GENERO = :2",
                [nuevo_nombre, id_genero]
            )
        conn.commit()
        print("Género actualizado exitosamente.")
    except Exception as e:
        print("Error al actualizar género:", e)

def eliminar_genero(conn):
    try:
        id_genero = int(input("Ingrese el ID del género a eliminar: "))
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM GENERO WHERE ID_GENERO = :1",
                [id_genero]
            )
        conn.commit()
        print("Género eliminado exitosamente.")
    except Exception as e:
        print("Error al eliminar género:", e)

def menu():
    conn = conectar()
    if not conn:
        return
    while True:
        print("\n--- Menú CRUD Género ---")
        print("1. Registrar Género")
        print("2. Listar Géneros")
        print("3. Actualizar Género")
        print("4. Eliminar Género")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_genero(conn)
        elif opcion == "2":
            listar_generos(conn)
        elif opcion == "3":
            actualizar_genero(conn)
        elif opcion == "4":
            eliminar_genero(conn)
        elif opcion == "5":
            conn.close()
            print("Conexión cerrada. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()