from Atleta import Atleta

def mostrar_menu():
    """Muestra el menú de opciones para la gestión de los Atletas."""
    print("\n--- Menú de Atletas ---")
    print("1. Agregar atleta")
    print("2. Consultar atleta")
    print("3. Editar atleta")
    print("4. Eliminar atleta")
    print("5. Salir")

def solicitar_datos_atleta():
    """Solicita al usuario los datos de un atleta.

    Returns:
        list: Una lista con los datos del atleta en el siguiente orden:
            [IDAtleta, Nombre, Apellido Paterno, Apellido Materno (si cuenta con él), Nacionalidad,
            Fecha de Nacimiento, Disciplina, Genero, Teléfono, Correo].
    """
    id = input("ID: ")
    nombre = input("Nombre: ")
    apellido_paterno = input("Apellido Paterno: ")
    apellido_materno = input("Apellido Materno: ")
    nacionalidad = input("Nacionalidad: ")
    fecha_nacimiento = input("Fecha de Nacimiento (YYYY-MM-DD): ")
    disciplina = input("Disciplina: ")
    genero = input("Genero: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    return [id, nombre, apellido_paterno, apellido_materno, nacionalidad, fecha_nacimiento, disciplina, genero, telefono, correo]

def main():
    """Función principal que maneja la interacción con el usuario.

    Esta función se encarga de mostrar el menú, procesar la opción seleccionada 
    por el usuario, y realizar las acciones correspondientes (agregar, 
    consultar, editar, o eliminar entrenadores).
    """
    atleta = Atleta()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            datos = solicitar_datos_atleta()
            try:
                atleta.validar_entrada(datos) 
                atleta.agregar_datos(datos)
            except ValueError as e:
                print(f"Error en los datos ingresados: {e}")
        elif opcion == '2':
            id = input("Ingresa el ID del atleta a consultar: ")
            atleta.consultar_datos(id)
        elif opcion == '3':
            id = input("Ingresa el ID del atleta a editar: ")
            campo = input("Ingresa el nombre del campo a editar: ")
            valor = input("Ingresa el nuevo valor: ")
            atleta.editar_datos(id, campo, valor)
        elif opcion == '4':
            id = input("Ingresa el ID del atleta a eliminar: ")
            atleta.eliminar_datos(id)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")