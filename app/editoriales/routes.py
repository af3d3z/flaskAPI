from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.libros.routes import ficheroLibros
from datos import leer_fichero, escribir_fichero
from models.Editorial import Editorial

editoriales_bp = Blueprint('editoriales', __name__)

ficheroEditoriales = "app/editoriales/editoriales.json"

@editoriales_bp.get('/')
def get_editoriales():
    return jsonify(leer_fichero(ficheroEditoriales))


@editoriales_bp.get('/<int:id>')
def get_editorial(id):
    for n in leer_fichero(ficheroEditoriales):
        if n['id'] == id:
            return jsonify(n)

    return jsonify({'error': 'not found'})


@editoriales_bp.get('/<int:id>/libros')
def get_editoriales_libros(id):
    lista = []
    libros = leer_fichero(ficheroLibros)
    for libro in libros:
        if libro['id'] == id:
            lista.append(libro)
    if len(lista) > 0:
        return lista, 200
    else:
        return {"error": "Esta editorial no tiene libros."}, 404


@editoriales_bp.post('/')
@jwt_required()
def add_editorial():
    if request.is_json:
        editoriales = leer_fichero(ficheroEditoriales)
        editorial_json = request.get_json()
        editorial = Editorial(id=editorial_json['id'], cif=editorial_json['cif'], razon=editorial_json['razon'],
                              direccion=editorial_json['direccion'], web=editorial_json['web'],
                              correo=editorial_json['correo'], tlf=editorial_json['tlf'])
        editoriales.append(editorial.serialize())
        escribir_fichero(ficheroEditoriales, editoriales)
        return editorial.serialize(), 201
    else:
        return '{error: "JSON invalido"}', 501


@editoriales_bp.put('/<int:id>')
@editoriales_bp.patch('/<int:id>')
@jwt_required()
def modify_editorial(id):
    if request.is_json:
        editorial_json = request.get_json()
        editoriales = leer_fichero(ficheroEditoriales)
        # consultar la editorial en el fichero
        editorial_found = next((editorial for editorial in editoriales if editorial['id'] == id), None)

        if editorial_found:
            # actualiza la editorial obtenida
            for key, value in editorial_json.items():
                editorial_found[key] = value

            escribir_fichero(ficheroEditoriales, editoriales)
            return editorial_found, 200
        else:
            return {"error": "Editorial not found"}, 404
    else:
        return {"error": "Invalid JSON"}, 400

@editoriales_bp.delete('/<int:id>')
@jwt_required()
def delete_editorial(id):
    editoriales = leer_fichero(ficheroEditoriales)
    for editorial in editoriales:
        if editorial['id'] == id:
            editoriales.remove(editorial)
            escribir_fichero(ficheroEditoriales, editoriales)
            return editorial, 200