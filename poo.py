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
