class Libro:
    def __init__(self, id, precio, isbn, titulo, numpag, tematica, id_editorial):
        self.id = id
        self.precio = precio
        self.isbn = isbn
        self.titulo = titulo
        self.numpag = numpag
        self.tematica = tematica
        self.id_editorial = id_editorial

    def __str__(self):
        return (f"ID: {self.id} Precio: {self.precio}€ Titulo: {self.titulo} Nº Páginas: {self.numpag} Temática: {self.tematica}"
                f"ID Editorial: {self.id_editorial}")
