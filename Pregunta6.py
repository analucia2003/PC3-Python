class Producto:
    def __init__(self, nombre, precio, año):
        # Inicializar los atributos del producto
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def __str__(self):
        # Método para mostrar la información del producto
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Año: {self.año}"

class Catálogo:
    def __init__(self):
        # Inicializar una lista para almacenar productos
        self.productos = []

    # Método para agregar un producto al catálogo
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Método para mostrar todos los productos del catálogo
    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    # Funcionalidad adicional 1: Filtrar productos por año
    def filtrar_por_año(self, año):
        print(f"Productos del año {año}:")
        for producto in self.productos:
            if producto.año == año:
                print(producto)

    # Funcionalidad adicional 2: Filtrar productos por rango de precio
    def filtrar_por_precio(self, precio_min, precio_max):
        print(f"Productos con precio entre ${precio_min} y ${precio_max}:")
        for producto in self.productos:
            if precio_min <= producto.precio <= precio_max:
                print(producto)

# Crear tres objetos de tipo Producto
producto1 = Producto("Televisor", 4000, 2021)
producto2 = Producto("Tablet", 1000, 2020)
producto3 = Producto("Laptop", 2000, 2020)

# Crear un objeto de tipo Catálogo
catalogo = Catálogo()

# Agregar los productos al catálogo
catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

# Mostrar todos los productos en el catálogo
print("Todos los productos en el catálogo:")
catalogo.mostrar_productos()

# Filtrar productos por año
catalogo.filtrar_por_año(2020)

# Filtrar productos por rango de precio
catalogo.filtrar_por_precio(1000, 2000)
