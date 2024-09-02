# Importar los menús específicos
from MenuDeEntrenador import main as menu_entrenador
from MenuDeAtleta import main as menu_atleta
from MenuDeDisciplina import main as menu_disciplina

def mostrar_menu_principal():
    """Muestra el menú principal para seleccionar la entidad a gestionar."""
    print("\n--- Menú Principal ---")
    print("1. Menú de Entrenador")
    print("2. Menú de Atleta")
    print("3. Menú de Disciplina")
    print("4. Salir")

def main():
    """Función principal que permite seleccionar la entidad a gestionar."""
    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            print("Accediendo al menú de Entrenador...")
            menu_entrenador()  # Accede al menú de Entrenador
        elif opcion == '2':
            print("Accediendo al menú de Atleta...")
            menu_atleta()  # Accede al menú de Atleta
        elif opcion == '3':
            print("Accediendo al menú de Disciplina...")
            menu_disciplina()  # Accede al menú de Disciplina
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()