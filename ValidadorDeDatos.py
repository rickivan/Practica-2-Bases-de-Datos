import re
from datetime import datetime

class ValidadorDeDatos:
    """Clase para validar diferentes tipos de datos."""

    def correo_valido(self, correos):
        """Valida una lista de correos electrónicos.

        Args:
            correos (list): Lista de correos electrónicos a validar.

        Returns:
            bool: True si todos los correos son válidos, False en caso contrario.
        """
        patron = re.compile(r'^[^@,]+@[a-zA-Z]+\.[a-zA-Z]+$')
        for correo in correos:
            if not patron.match(correo):
                print(f"El correo '{correo}' no es válido, verifica que los correos sean correctos.")
                return False
        return True

    def telefono_valido(self, telefonos):
        """Valida una lista de números de teléfono.

        Args:
            telefonos (list): Lista de números de teléfono a validar.

        Returns:
            bool: True si todos los números de teléfono son válidos, False en caso contrario.
        """
        patron = re.compile(r'^\d{10}$')
        for telefono in telefonos:
            if not patron.match(telefono):
                print(f"Verifica que el número de teléfono '{telefono}' tenga 10 dígitos.")
                return False
        return True

    def hay_campo_vacio(self, datos, atributos, excepciones):
        """Verifica si hay campos vacíos en los datos proporcionados, salvo las excepciones.

        Args:
            datos (list): Lista de datos a verificar.
            atributos (list): Lista de atributos esperados.
            excepciones (list): Lista de atributos que pueden estar vacíos.

        Returns:
            bool: True si hay campos vacíos que no están en la lista de excepciones, False en caso contrario.
        """
        for i, dato in enumerate(datos):
            if atributos[i] not in excepciones:
                if dato == "":
                    print("Verifica que los campos se han llenado correctamente.")
                    return True
        return False

    def datos_completos(self, datos, atributos):
        """Verifica que el número de datos ingresados sea correcto (puede incluir campos vacíos).

        Args:
            datos (list): Lista de datos a verificar.
            atributos (list): Lista de atributos esperados.

        Returns:
            bool: True si el número de datos coincide con el número de atributos, False en caso contrario.
        """
        if len(datos) != len(atributos):
            print("Verifique que el número de datos ingresados sea correcto.")
            return False
        return True

    def id_numerico_valido(self, id):
        """Verifica si el ID proporcionado es un número entero válido.

        Args:
            id (str): ID a verificar.

        Returns:
            bool: True si el ID es un número entero válido, False en caso contrario.
        """
        try:
            int(id)
            return True
        except ValueError:
            print(f"Error al procesar el ID: {id}")
            return False

    def formato_fecha_valida(self, fecha):
        """Valida el formato de la fecha en el formato YYYY-MM-DD usando datetime.

        Args:
            fecha (str): Fecha a verificar.

        Returns:
            bool: True si la fecha tiene el formato correcto, False en caso contrario.
        """
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return True
        except ValueError:
            print(f"Error en el formato de fecha {fecha}.")
            return False
