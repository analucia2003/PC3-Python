def obtener_calificaciones():
    while True:
        try:
            # Solicitar al usuario una lista de calificaciones separadas por comas
            calificaciones_input = input("Ingrese una lista de calificaciones separadas por comas: ")
            
            # Dividir la cadena en una lista
            calificaciones_str = calificaciones_input.split(',')
            
            # Convertir cada calificación a float y luego redondear a entero
            calificaciones = [round(float(c.strip())) for c in calificaciones_str]
            
            # Retornar la lista de calificaciones enteras
            return calificaciones

        except ValueError:
            # Informar al usuario si hay un error de conversión
            print("Error: Asegúrese de ingresar solo números, sin letras. Intente nuevamente.")

if __name__ == '__main__':
    calificaciones = obtener_calificaciones()
    print(f"Calificaciones ingresadas: {calificaciones}")
