def obtener_combustible():
    while True:
        try:
            # Solicitar al usuario una fracción en formato X/Y
            fraccion = input("Ingrese una fracción en formato X/Y (Ejemplo 3/4): ")
            x, y = fraccion.split('/')
            
            # Convertir a enteros
            x = int(x)
            y = int(y)

            # Validar que X sea menor o igual a Y y que Y no sea 0
            if x > y:
                print("Error: X debe ser menor o igual a Y. Intente nuevamente.")
                continue
            if y == 0:
                raise ZeroDivisionError

            # Calcular el porcentaje
            porcentaje = round((x / y) * 100)

            # Manejo de casos especiales
            if porcentaje < 1:
                return "E"
            elif porcentaje > 99:
                return "F"
            else:
                return f"{porcentaje}%"

        except ValueError:
            print("Error: Solo se permiten números enteros. Intente nuevamente.")
        except ZeroDivisionError:
            print("Error: El denominador no puede ser cero. Intente nuevamente.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}. Intente nuevamente.")

if __name__ == '__main__':
    resultado = obtener_combustible()
    print(f"Output: {resultado}")
