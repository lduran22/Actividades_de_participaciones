class Libro:
    def __init__(self, titulo, isbn, precio, existencias):
        self.titulo = titulo
        self.isbn = isbn
        self.precio = precio
        self.existencias = existencias

    def __str__(self):
        return f"{self.titulo} (ISBN: {self.isbn}, Precio: {self.precio}, Existencias: {self.existencias})"