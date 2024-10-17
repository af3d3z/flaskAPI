from flask import Blueprint, jsonify, request

from models.Libro import Libro

libros_bp = Blueprint('libros_bp', __name__)

libros = [
    {"id": 1, "precio": 15, "isbn": "978-7-2398-8924-8", "titulo": "Black Hat Go", "numpag": 345, "tematica": "Tecnología", "id_editorial": 1},
    {"id": 2, "precio": 20, "isbn": "968-3-2338-6783-0", "titulo": "Python deep learning", "numpag": 234, "tematica": "Tecnología", "id_editorial": 2}
]

@libros_bp.get('/libros')
def get_libros():
    return jsonify(libros)



@libros_bp.get('/libros/<int:id>')
def get_libro(id):
    for n in libros:
        if n['id'] == id:
            return jsonify(n)

    return jsonify({'error': 'not found'})




@libros_bp.post('/libros')
def add_libro():
    if request.is_json:
        libro_json = request.get_json()
        libro = Libro(id=libro_json['id'], precio=libro_json['precio'], isbn=libro_json['isbn'],
                      titulo=libro_json['titulo'], numpag=libro_json['numpag'], tematica=libro_json['tematica'], id_editorial=libro_json['id_editorial'])
        libros.append(libro.serialize())
        return libro.serialize(), 201
    else:
        return '{error: "JSON invalido"}', 501





@libros_bp.put('/libros/<int:id>')
@libros_bp.patch('/libros/<int:id>')
def modify_libro(id):
    if request.is_json:
        libro_json = request.get_json()
        for libro in libros:
            if libro['id'] == id:
                for element in libro_json:
                    libro[element] = libro_json[element]
                return libro_json, 200
    else:
        return {"error": "JSON invalido"}


@libros_bp.delete('/libros/<int:id>')
def delete_libro(id):
    for libro in libros:
        if libro['id'] == id:
            libros.remove(libro)
            return libro, 200
