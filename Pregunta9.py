import math

# Reutilización de la clase CIRCULO
class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

# Reutilización de la clase RECTANGULO
class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

# Reutilización de la clase CUADRADO que hereda de RECTANGULO
class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)

# Función para validar entradas
def validar_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Error: El número debe ser positivo.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Menú principal
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            radio = validar_numero_positivo("Ingrese el radio del círculo: ")
            circulo = CIRCULO(radio)
            print(f"El área del círculo es: {circulo.calcular_area():.2f}")

        elif opcion == "2":
            largo = validar_numero_positivo("Ingrese el largo del rectángulo: ")
            ancho = validar_numero_positivo("Ingrese el ancho del rectángulo: ")
            rectangulo = RECTANGULO(largo, ancho)
            print(f"El área del rectángulo es: {rectangulo.calcular_area():.2f}")

        elif opcion == "3":
            lado = validar_numero_positivo("Ingrese el lado del cuadrado: ")
            cuadrado = CUADRADO(lado)
            print(f"El área del cuadrado es: {cuadrado.calcular_area():.2f}")

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
