import csv
import os
from Entidad import Entidad
from datetime import datetime

class Atleta(Entidad):
    """Clase para gestionar la información de Atletaes.

    Esta clase maneja la creación, consulta, edición y eliminación de 
    información de Atletaes almacenada en un archivo CSV.

    Attributes:
        archivo (str): Ruta al archivo CSV donde se almacenan los datos de los Atletaes.
    """

    archivo = ""

    def __init__(self):
        """Inicializa la clase Atleta.

        Establece la ruta del archivo CSV y crea el archivo si no existe.
        """
        self.archivo = "archivos/Atleta.csv"
        if not os.path.exists(self.archivo):
            self.__inicializar_archivo()


    def __inicializar_archivo(self):
        """Inicializa el archivo CSV con los encabezados correspondientes a un Atleta.

        Si el archivo CSV no existe, lo crea con los encabezados necesarios.
        """
        with open(self.archivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nombre', 'Apellido Paterno', 'Apellido Materno', 
                             'Nacionalidad', 'Fecha de nacimiento', 
                             'Disciplina','Género', 'Teléfono', 'Correo'])


    def __exist(self, id):
        """Verifica si un Atleta con un ID específico existe en el archivo.

        Args:
            id (int): ID del Atleta a verificar.

        Returns:
            bool: True si el Atleta existe, False en caso contrario.
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

    def validar_entrada(self, datos):
        """Valida los datos de entrada de un entrenador.

        Args:
        datos (list): Lista con los datos del entrenador.

        Raises:
        ValueError: Si alguno de los datos no cumple con el tipo esperado o el formato.
        """
        if len(datos) != 10:
            raise ValueError("La lista de datos debe contener exactamente 9 elementos.")

        try:
            datos[0] = int(datos[0])  # Validar que el ID sea un entero
        except ValueError:
            raise ValueError("El ID debe ser un número entero.")
    
        if not all(isinstance(datos[i], str) for i in range(1, 9)):
            raise ValueError("Nombre, Apellidos, Nacionalidad, Disciplina, Género deben ser cadenas de texto.")
    
        try:
            datos[8] = int(datos[8])  # Validar que el Teléfono sea un entero
        except ValueError:
            raise ValueError("El Teléfono debe ser un número entero.")
    
        if not self.validar_formato_fecha(datos[5]):
            raise ValueError("La Fecha de Nacimiento debe estar en el formato YYYY-MM-DD.")
    
    def validar_formato_fecha(self, fecha):
        """Valida el formato de la fecha en el formato YYYY-MM-DD usando datetime."""
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return True
        except ValueError:
            return False


    def agregar_datos(self, datos):
        """Agrega un nuevo Atleta al archivo CSV.

        Verifica si el ID ya existe antes de agregar el nuevo Atleta.

        Args:
            datos (list): Lista con los datos del Atleta en el orden 
            ['ID', 'Nombre', 'Apellido Paterno', 'Apellido Materno', 
             'Nacionalidad', 'Fecha de nacimiento', 'Género', 
             'Teléfono', 'Correo'].

        Raises:
            ValueError: Si el ID no es un número entero válido.
        """
        try:
            id = int(datos[0])
            if self.__exist(id):
                print(f"El Atleta con ID {id} ya está registrado.")
                return
        except ValueError as e:
            print(f"Error al procesar los datos: {e}")
            return

        try:
            with open(self.archivo, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(datos)

            print(f"Atleta registrado exitosamente.")
        except Exception as e:
            print(f"Error al registrar al Atleta: {e}")


    def consultar_datos(self, id):
        """Consulta la información de un Atleta por ID.

        Args:
            id (int): ID del Atleta a consultar.

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
                print(f"No fue posible encontrar un Atleta con ID: {id}.")
        except Exception as e:
            print(f"Error al consultar al Atleta con ID: {id}")


    def editar_datos(self, id, campo, valor):
        """Edita la información de un Atleta en el archivo CSV.

        Args:
            id (int): ID del Atleta a editar.
            campo (str): Campo que se desea editar.
            valor (str): Nuevo valor para el campo.

        Raises:
            Exception: Si ocurre un error al leer o escribir en el archivo.
        """
        if not self.__exist(id):
            print(f"El Atleta con ID {id} no está registrado.")
            return

        if campo == 'ID':
            print(f"No es posible modificar el ID del Atleta.")
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

            print(f"{campo} del Atleta editado exitosamente.")
        except Exception as e:
            print(f"Error al editar el Atleta con ID {id}: {e}")
            if os.path.exists(temp_archivo):
                os.remove(temp_archivo)

    def eliminar_datos(self, id):
        """Elimina un Atleta del archivo CSV por su ID.

        Args:
            id (int): ID del Atleta a eliminar.

        Raises:
            Exception: Si ocurre un error al leer o escribir en el archivo.
        """
        if not self.__exist(id):
            print(f"El Atleta con ID {id} no está registrado.")
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

            print(f"Atleta con ID {id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar el Atleta con ID {id}: {e}")
            if os.path.exists(temp_archivo):
                os.remove(temp_archivo)
