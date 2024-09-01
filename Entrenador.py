import csv
import os
from Entidad import Entidad

class Entrenador(Entidad):
    """Clase para gestionar la información de entrenadores.

    Esta clase maneja la creación, consulta, edición y eliminación de 
    información de entrenadores almacenada en un archivo CSV.

    Attributes:
        archivo (str): Ruta al archivo CSV donde se almacenan los datos de los entrenadores.
    """

    archivo = ""

    def __init__(self):
        """Inicializa la clase Entrenador.

        Establece la ruta del archivo CSV y crea el archivo si no existe.
        """
        self.archivo = "archivos/entrenador.csv"
        if not os.path.exists(self.archivo):
            self.__inicializar_archivo()


    def __inicializar_archivo(self):
        """Inicializa el archivo CSV con los encabezados correspondientes a un entrenador.

        Si el archivo CSV no existe, lo crea con los encabezados necesarios.
        """
        with open(self.archivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nombre', 'Apellido Paterno', 'Apellido Materno', 
                             'Nacionalidad', 'Fecha de nacimiento', 'Atleta', 
                             'Disciplina', 'Teléfono', 'Correo'])


    def __exist(self, id):
        """Verifica si un entrenador con un ID específico existe en el archivo.

        Args:
            id (int): ID del entrenador a verificar.

        Returns:
            bool: True si el entrenador existe, False en caso contrario.
        """
        try:
            with open(self.archivo, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['ID'] == str(id):
                        return True
                return False
        except Exception:
            return False


    def agregar_datos(self, datos):
        """Agrega un nuevo entrenador al archivo CSV.

        Verifica si el ID ya existe antes de agregar el nuevo entrenador.

        Args:
            datos (list): Lista con los datos del entrenador en el orden 
            ['ID', 'Nombre', 'Apellido Paterno', 'Apellido Materno', 
             'Nacionalidad', 'Fecha de nacimiento', 'Atleta', 
             'Disciplina', 'Teléfono', 'Correo'].

        Raises:
            ValueError: Si el ID no es un número entero válido.
        """
        try:
            id = int(datos[0])
            if self.__exist(id):
                print(f"El entrenador con ID {id} ya está registrado.")
                return
        except ValueError as e:
            print(f"Error al procesar los datos: {e}")
            return

        try:
            with open(self.archivo, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(datos)

            print(f"Entrenador registrado exitosamente.")
        except Exception as e:
            print(f"Error al registrar al entrenador: {e}")


    def consultar_datos(self, id):
        """Consulta la información de un entrenador por ID.

        Args:
            id (int): ID del entrenador a consultar.

        Raises:
            Exception: Si ocurre un error al leer el archivo.
        """
        try:
            with open(self.archivo, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['ID'] == id:
                        print(row)
                        return
                print(f"No fue posible encontrar un entrenador con ID: {id}.")
        except Exception as e:
            print(f"Error al consultar al entrenador con ID: {id}")


    def editar_datos(self, id, campo, valor):
        """Edita la información de un entrenador en el archivo CSV.

        Args:
            id (int): ID del entrenador a editar.
            campo (str): Campo que se desea editar.
            valor (str): Nuevo valor para el campo.

        Raises:
            Exception: Si ocurre un error al leer o escribir en el archivo.
        """
        if not self.__exist(id):
            print(f"El entrenador con ID {id} no está registrado.")
            return

        if campo == 'ID':
            print(f"No es posible modificar el ID del entrenador.")
            return

        temp_archivo = 'archivos/temp.csv'

        try:
            with open(self.archivo, mode='r') as file, open(temp_archivo, mode='w', newline='') as temp_file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    if row['ID'] == id:
                        row[campo] = valor
                    writer.writerow(row)

            os.remove(self.archivo)
            os.rename(temp_archivo, self.archivo)

            print(f"{campo} del entrenador editado exitosamente.")
        except Exception as e:
            print(f"Error al editar el entrenador con ID {id}: {e}")
            if os.path.exists(temp_archivo):
                os.remove(temp_archivo)

    def eliminar_datos(self, id):
        """Elimina un entrenador del archivo CSV por su ID.

        Args:
            id (int): ID del entrenador a eliminar.

        Raises:
            Exception: Si ocurre un error al leer o escribir en el archivo.
        """
        if not self.__exist(id):
            print(f"El entrenador con ID {id} no está registrado.")
            return

        temp_archivo = 'archivos/temp.csv'

        try:
            with open(self.archivo, mode='r') as file, open(temp_archivo, mode='w', newline='') as temp_file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    if row['ID'] != id:
                        writer.writerow(row)

            os.remove(self.archivo)
            os.rename(temp_archivo, self.archivo)

            print(f"Entrenador con ID {id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar el entrenador con ID {id}: {e}")
            if os.path.exists(temp_archivo):
                os.remove(temp_archivo)
