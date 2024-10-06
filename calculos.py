import Pregunta8

# Ejemplos de uso de las funciones del módulo operaciones
a = 9
b = 3
c = "Texto"  # Valor no válido para probar el manejo de errores

# Suma
print(f"Suma de {a} y {b}: {Pregunta8.suma(a, b)}")
print(f"Suma de {a} y {c}: {Pregunta8.suma(a, c)}")

# Resta
print(f"Resta de {a} y {b}: {Pregunta8.resta(a, b)}")
print(f"Resta de {a} y {c}: {Pregunta8.resta(a, c)}")

# Producto
print(f"Producto de {a} y {b}: {Pregunta8.producto(a, b)}")
print(f"Producto de {a} y {c}: {Pregunta8.producto(a, c)}")

# División
print(f"División de {a} entre {b}: {Pregunta8.division(a, b)}")
print(f"División de {a} entre 0: {Pregunta8.division(a, 0)}")
print(f"División de {a} entre {c}: {Pregunta8.division(a, c)}")
