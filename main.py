from libro import Libro
from gestión import GestionBiblioteca

def menu():
    biblioteca = GestionBiblioteca()

    while True:
        print("\n--- Menú Biblioteca ---")
        print("1. Agregar un libro a la biblioteca")
        print("2. Listar los libros en la biblioteca")
        print("3. Buscar un libro por su título")
        print("4. Buscar un libro por su autor")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            print("\nListado de libros en la biblioteca:")
            biblioteca.listar_libros()

        elif opcion == "3":
            titulo = input("Ingrese el título del libro que desea buscar: ")
            biblioteca.buscar_por_titulo(titulo)

        elif opcion == "4":
            autor = input("Ingrese el nombre del autor que desea buscar: ")
            biblioteca.buscar_por_autor(autor)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
