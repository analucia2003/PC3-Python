class Libro:
    def __init__(self, titulo, autor, isbn):
        # Inicializamos los atributos del libro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        # Representación del libro como una cadena
        return f"Titulo: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}"
