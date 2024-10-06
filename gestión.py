class GestionBiblioteca:
    def __init__(self):
        # Inicializamos una lista vacía de libros
        self.libros = []

    def agregar_libro(self, libro):
        # Agregamos un libro a la lista de libros
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def listar_libros(self):
        # Listamos todos los libros en la biblioteca
        if self.libros:
            for libro in self.libros:
                print(libro)
        else:
            print("No hay libros en la biblioteca.")

    def buscar_por_titulo(self, titulo):
        # Buscamos un libro por su título
        encontrados = [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]
        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print(f"No se encontraron libros con el título '{titulo}'.")

    def buscar_por_autor(self, autor):
        # Buscamos libros por autor
        encontrados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print(f"No se encontraron libros del autor '{autor}'.")
