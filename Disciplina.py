import csv 
import os
from Entidad import Entidad

class Disciplina(Entidad):
    """Clase para gestionar la información de disciplinas.

    Esta clase maneja la creación, consulta, edición y eliminación de 
    información de disciplinas almacenada en un archivo CSV.

    Attributes:
        archivo (str): Ruta al archivo CSV donde se almacenan los datos de las disciplinas.
    """
    archivo = ""
    
    def __init__(self):
        """Inicializa la clase Disciplina.
        
        Establece la ruta del archivo CSV y crea el archivo si no existe"""
        self.archivo = "archivos/disciplina.csv"
        if not os.path.exists(self.archivo):
            self.__inicializar_archivo()

    def __inicializar_archivo(self):
        """Inicializa el archivo CSV con los encabezados correspondientes a una disciplina.

        Si el archivo CSV no existe, lo crea con los encabezados necesarios.
        """
        with open(self.archivo, mode='w', newline='') as file: 
            writer = csv.writer(file)
            writer.writerow(['Nombre', 'Categoria', 'Participantes', 'Patrocinadores'])
    
    def __exist(self, id):
        """Verifica si una disciplina con un nombre específico existe en el archivo.

        Args:
            id (String): Nombre de la disciplina a verificar.
            categoria (String): Nombre de la categoria a verificar.

        Returns:
            bool: True si la disciplina existe, False en caso contrario.
        """
        try:
            with open(self.archivo, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader: 
                    if row['Nombre']+' '+row['Categoria'] == str(id):
                        return True
                    return False
        except Exception as e:
            print(f"Ha ocurrido algun error: {e}")
    
    def agregar_datos(self, datos):
        """Agrega una nueva disciplina al archivo CSV.

        Verifica si el nombre ya existe antes de agregar la nueva disciplina.

        Args:
            datos (list): Lista con los datos de la disciplina en el orden 
            ['Nombre', 'Categoria', 'Participantes', 'Patrocinadores].
        """
        try: 
            id = datos[0]
            if self.__exist(id): 
                print(f"Ya se ha registrado la disciplina con ID {id}")
                return 
        except Exception as e:
            print(f"Error al procesar los datos: {e}")
            return
        try: 
            with open(self.archivo, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(datos)

            print(f"Disciplina agregada exitosamente.")
        except Exception as e: 
            print(f"Error al registrar la disciplina: {e}"
)
            
    def consultar_datos(self, id):
        """Consulta la información de una disciplina por nombre

        Args:
            id (String): Nombre de la disciplina a consultar.

        Raises:
            Exception: Si ocurre un error al leer el archivo.
        """
        try: 
            with open(self.archivo, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader: 
                    if row['Nombre'].lower() == id.lower():
                        print(row)
                        return
                print(f"No existe una disciplina con ese nombre")
        except Exception as e:
            print(f"Error al consultar la disciplina : {e}")

    def editar_datos(self, id, campo, valor):
        """Edita la información de una disciplina en el archivo CSV.

        Args:
            id (String): Nombre de la disciplina a editar.
            campo (String): Campo que se desea editar.
            valor (String): Nuevo valor para el campo.

        Raises:
            Exception: Si ocurre un error al leer o escribir en el archivo.
        """
        if not self.__exist(id):
            print(f"No se encontro la disciplina con nombre: {id}")
            return
        if campo == 'Nombre':
            print(f"No es posible modificar el nombre de la disciplina")
            return
        
        temp_archivo = 'archivos/temp.csv'

        try: 
            with open(self.archivo, mode='r') as file, open(temp_archivo, mode='w', newline='') as temp_file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(temp_file, fieldnames)
                writer.writeheader()
                for row in reader: 
                    if row['Nombre']+' '+row['Categoria'] == id:
                        row[campo] = valor
                    writer.writerow(row)
            os.remove(self.archivo)
            os.rename(temp_archivo, self.archivo)

            print(f"{campo} de la disciplina ha sido modificado")
        except Exception as e: 
            print(f"Error al editar la disciplina: {e}")
            if os.path.exists(temp_archivo):
                    os.remove(temp_archivo)

    def eliminar_datos(self, id):
        """Elimina una disciplina del archivo CSV por su nombre.

        Args:
            id (String): Nombre de la disciplina a eliminar.

        Raises:
            Exception: Si ocurre un error al leer o escribir en el archivo.
        """
        if not self.__exist(id):
            print(f"No se encontro la disciplina con nombre {id}")
            return 
        
        temp_archivo = 'archivos/temp.csv'

        try: 
            with open(self.archivo, mode='r') as file, open(temp_archivo, mode='w', newline='') as temp_file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader: 
                    if row['Nombre']+' '+row['Categoria'] != id:
                        writer.writerow(row)
            
            os.remove(self.archivo)
            os.rename(temp_archivo, self.archivo)

            print(f"Se ha eliminado la disciplina con nombre {id}")
        except Exception as e: 
            print(f"Error al eliminar la disciplina: {e}")
            if os.path.exists(temp_archivo):
                os.remove(temp_archivo)



