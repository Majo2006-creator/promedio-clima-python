# Programa para calcular el promedio semanal del clima
# Enfoque: Programación Tradicional

def ingresar_temperaturas():
    """
    Solicita al usuario ingresar las temperaturas de 7 días
    y las almacena en una lista.
    """
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio semanal a partir de una lista de temperaturas.
    """
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio


# Programa principal
temperaturas_semana = ingresar_temperaturas()
promedio_semanal = calcular_promedio(temperaturas_semana)

print(f"\nEl promedio semanal de temperatura es: {promedio_semanal:.2f} °C")
# Programa para calcular el promedio semanal del clima
# Enfoque: Programación Orientada a Objetos (POO)

class ClimaSemanal:
    """
    Clase que representa el registro del clima semanal.
    """

    def __init__(self):
        # Encapsulamiento del atributo temperaturas
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas de los 7 días.
        """
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método para calcular el promedio semanal.
        """
        return sum(self.__temperaturas) / len(self.__temperaturas)


# Programa principal
clima = ClimaSemanal()
clima.ingresar_temperaturas()
promedio = clima.calcular_promedio()

print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")
