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
