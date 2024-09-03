from Disciplina import Disciplina

def mostrar_menu_disciplina():
    """Muestra el menú de opciones para la gestión de las Disciplinas."""
    print("\n--- Menú de Disciplinas ---")
    print("1. Agregar Disciplina")
    print("2. Consultar Disciplina")
    print("3. Editar Disciplina")
    print("4. Eliminar Disciplina")
    print("5. Salir")
    
def solicitar_datos_disciplina():
    """Solicita al usuario los datos de una Disciplina.

    Returns:
        list: Una lista con los datos de la disciplina en el siguiente orden:
            [Nombre, Categoría, Participantes, Patrocinadores].
    """
    nombre = input("Nombre: ")
    categoria = input("Categoria: ")
    participantes = input("Participantes: ")
    patrocinadores = input("Patrocinadores: ")
    return [nombre, categoria, participantes, patrocinadores]

def main():
    """Función principal que maneja la interacción con el usuario.

    Esta función se encarga de mostrar el menú, procesar la opción seleccionada 
    por el usuario, y realizar las acciones correspondientes (agregar, 
    consultar, editar, o eliminar entrenadores).
    """
    disciplina = Disciplina()

    while True:
        mostrar_menu_disciplina()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            datos = solicitar_datos_disciplina()
            disciplina.agregar_datos(datos)
        elif opcion == '2':
            nombre = input("Ingresa el nombre de la disciplina a consultar: ")
            categoria = input("Ingresa la categoria de la disciplina a consultar: ")
            disciplina.consultar_datos(nombre, categoria)
        elif opcion == '3':
            nombre = input("Ingresa el nombre de la disciplina a editar: ")
            categoria = input("Ingresa la categoria de la disciplina a editar: ")
            campo = input("Ingresa el nombre del campo a editar: ")
            valor = input("Ingresa el nuevo valor: ")
            disciplina.editar_datos(nombre, categoria, campo, valor)
        elif opcion == '4':
            nombre = input("Ingresa el nombre de la disciplina a eliminar: ")
            categoria = input("Ingresa la categoria de la disciplina a eliminar: ")
            disciplina.eliminar_datos(nombre, categoria)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")