from carro_compra import CarroCompras
from libro import Libro
from libro_existente_error import LibroExistenteError
from libro_agotado_error import LibroAgotadoError
from existencias_insuficientes_error import ExistenciasInsuficientesError

class TiendaLibros:
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()

    def adicionar_libro_a_catalogo(self, isbn, titulo, precio, existencias):
        if isbn in self.catalogo:
            raise LibroExistenteError(titulo, isbn)
        
        libro = Libro(titulo, isbn, precio, existencias)
        self.catalogo[isbn] = libro
        return libro

    def agregar_libro_a_carrito(self, libro, cantidad):
        if libro.existencias <= 0:
            raise LibroAgotadoError(libro.titulo, libro.isbn)
        if libro.existencias < cantidad:
            raise ExistenciasInsuficientesError(libro.titulo, libro.isbn, cantidad)

        libro.existencias -= cantidad
        self.carrito.agregar_item(libro, cantidad)

    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)