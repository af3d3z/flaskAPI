from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from datos import leer_fichero, escribir_fichero
from models.Libro import Libro

libros_bp = Blueprint('libros_bp', __name__)


ficheroLibros = "app/libros/libros.json"

@libros_bp.get('/')
def get_libros():
    return jsonify(leer_fichero(ficheroLibros))


@libros_bp.get('/<int:id>')
def get_libro(id):
    for n in leer_fichero(ficheroLibros):
        if n['id'] == id:
            return jsonify(n)

    return jsonify({'error': 'not found'})


@libros_bp.post('/')
@jwt_required()
def add_libro():
    if request.is_json:
        libros = leer_fichero(ficheroLibros)
        libro_json = request.get_json()
        libro = Libro(id=libro_json['id'], precio=libro_json['precio'], isbn=libro_json['isbn'],
                      titulo=libro_json['titulo'], numpag=libro_json['numpag'], tematica=libro_json['tematica'], id_editorial=libro_json['id_editorial'])
        libros.append(libro.serialize())
        escribir_fichero(ficheroLibros, libros)
        return libro.serialize(), 201
    else:
        return '{error: "JSON invalido"}', 501



@libros_bp.put('/<int:id>')
@libros_bp.patch('/<int:id>')
@jwt_required()
def modify_libro(id):
    if request.is_json:
        libros = leer_fichero(ficheroLibros)
        libro_json = request.get_json()

        # consultar el libro en el fichero
        libro_found = next((libro for libro in libros if libro['id'] == id), None)

        if libro_found:
            # actualiza el libro obtenido
            for key, value in libro_json.items():
                libro_found[key] = value

            escribir_fichero(ficheroLibros, libros)
            return libro_found, 200
        else:
            return {"error": "Book not found"}, 404

    else:
        return {"error": "JSON invalido"}


@libros_bp.delete('/<int:id>')
@jwt_required()
def delete_libro(id):
    libros = leer_fichero(ficheroLibros)
    for libro in libros:
        if libro['id'] == id:
            libros.remove(libro)
            escribir_fichero(ficheroLibros, libros)
            return libro, 200

    return {"error": "Libro not found"}, 404

