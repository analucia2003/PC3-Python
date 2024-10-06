import math

class CIRCULO:
    def __init__(self, radio):
        # Inicializar el atributo radio
        self.radio = radio

    def calcular_area(self):
        # Calcular el área utilizando la fórmula del área del círculo: π * radio^2
        return math.pi * (self.radio ** 2)

# Crear dos objetos de tipo CIRCULO
circulo1 = CIRCULO(4)
circulo2 = CIRCULO(3)

# Calcular y mostrar el área de cada círculo
print(f"El área del círculo 1 con radio 4 es: {circulo1.calcular_area():.2f}")
print(f"El área del círculo 2 con radio 3 es: {circulo2.calcular_area():.2f}")
