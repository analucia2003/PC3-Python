import math

class Punto:
    def __init__(self, x=0, y=0):
        # Inicializar las coordenadas X y Y
        self.x = x
        self.y = y

    # Método string para mostrar el punto en formato (X, Y)
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Método para determinar en qué cuadrante se encuentra el punto
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "El punto está en el primer cuadrante."
        elif self.x < 0 and self.y > 0:
            return "El punto está en el segundo cuadrante."
        elif self.x < 0 and self.y < 0:
            return "El punto está en el tercer cuadrante."
        elif self.x > 0 and self.y < 0:
            return "El punto está en el cuarto cuadrante."
        elif self.x == 0 and self.y != 0:
            return "El punto está sobre el eje Y."
        elif self.x != 0 and self.y == 0:
            return "El punto está sobre el eje X."
        else:
            return "El punto está en el origen."

    # Método para calcular el vector entre dos puntos
    def vector(self, otro_punto):
        return (otro_punto.x - self.x, otro_punto.y - self.y)

    # Método opcional: calcular la distancia entre dos puntos
    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)

class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
        # Inicializar los puntos que forman la diagonal del rectángulo
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    # Método para calcular la base del rectángulo
    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)

    # Método para calcular la altura del rectángulo
    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)

    # Método para calcular el área del rectángulo
    def area(self):
        return self.base() * self.altura()

# Crear dos puntos
punto1 = Punto(3, 4)
punto2 = Punto(4, 5)

# Mostrar información de los puntos
print(f"Punto 1: {punto1}")
print(f"Punto 2: {punto2}")

# Determinar en qué cuadrante están los puntos
print(punto1.cuadrante())
print(punto2.cuadrante())

# Calcular el vector entre dos puntos
vector = punto1.vector(punto2)
print(f"Vector entre Punto 1 y Punto 2: {vector}")

# Calcular la distancia entre dos puntos
distancia = punto1.distancia(punto2)
print(f"Distancia entre Punto 1 y Punto 2: {distancia:.2f}")

# Crear un rectángulo usando dos puntos
rectangulo = Rectangulo(punto1, punto2)

# Mostrar la base, altura y área del rectángulo
print(f"Base del rectángulo: {rectangulo.base()}")
print(f"Altura del rectángulo: {rectangulo.altura()}")
print(f"Área del rectángulo: {rectangulo.area()}")

