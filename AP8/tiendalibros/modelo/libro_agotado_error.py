from tiendalibros.modelo.libro_error import LibroError


class LibroAgotadoError(LibroError):
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        super().__init__(f"El libro con título '{titulo}' y ISBN: '{isbn}' está agotado.")

    def __str__(self):
        return f"El libro con título '{self.titulo}' y ISBN: '{self.isbn}' está agotado."
