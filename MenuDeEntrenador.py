from Entrenador import Entrenador

def mostrar_menu():
    """Muestra el menú de opciones para la gestión de entrenadores."""
    print("\n--- Menú de Entrenadores ---")
    print("1. Agregar entrenador")
    print("2. Consultar entrenador")
    print("3. Editar entrenador")
    print("4. Eliminar entrenador")
    print("5. Salir")

def solicitar_datos_entrenador():
    """Solicita al usuario los datos de un entrenador.

    Returns:
        list: Una lista con los datos del entrenador en el siguiente orden:
            [ID, Nombre, Apellido Paterno, Apellido Materno, Nacionalidad,
            Fecha de Nacimiento, Atleta, Disciplina, Teléfono, Correo].
    """
    id = input("ID: ")
    nombre = input("Nombre: ")
    apellido_paterno = input("Apellido Paterno: ")
    apellido_materno = input("Apellido Materno: ")
    nacionalidad = input("Nacionalidad: ")
    fecha_nacimiento = input("Fecha de Nacimiento (YYYY-MM-DD): ")
    atleta = input("Atleta: ")
    disciplina = input("Disciplina: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    return [id, nombre, apellido_paterno, apellido_materno, nacionalidad, fecha_nacimiento, atleta, disciplina, telefono, correo]

def main():
    """Función principal que maneja la interacción con el usuario.

    Esta función se encarga de mostrar el menú, procesar la opción seleccionada 
    por el usuario, y realizar las acciones correspondientes (agregar, 
    consultar, editar, o eliminar entrenadores).
    """
    entrenador = Entrenador()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            datos = solicitar_datos_entrenador()
            entrenador.agregar_datos(datos)
        elif opcion == '2':
            id = input("Ingresa el ID del entrenador a consultar: ")
            entrenador.consultar_datos(id)
        elif opcion == '3':
            id = input("Ingresa el ID del entrenador a editar: ")
            campo = input("Ingresa el nombre del campo a editar: ")
            valor = input("Ingresa el nuevo valor: ")
            entrenador.editar_datos(id, campo, valor)
        elif opcion == '4':
            id = input("Ingresa el ID del entrenador a eliminar: ")
            entrenador.eliminar_datos(id)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()
