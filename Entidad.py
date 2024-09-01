from abc import ABC, abstractmethod

class Entidad(ABC):
    """Interfaz que define los métodos básicos para gestionar entidades."""

    @abstractmethod
    def agregar_datos(self, datos):
        """Agrega una nueva entidad."""
        pass

    @abstractmethod
    def consultar_datos(self, id):
        """Consulta la información de una entidad por su ID."""
        pass

    @abstractmethod
    def editar_datos(self, id, campo, valor):
        """Edita la los datos de un campo de una entidad."""
        pass

    @abstractmethod
    def eliminar_datos(self, id):
        """Elimina una entidad por su ID."""
        pass