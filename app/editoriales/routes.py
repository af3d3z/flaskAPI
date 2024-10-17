from flask import Blueprint, jsonify, request

from models.Editorial import Editorial

editoriales_bp = Blueprint('editoriales', __name__)


editoriales = [
    {"id": 1, "cif": 123456789, "razon": "Manolo Books", "web": "https://manolobooks.com",
     "correo": "info@manolobooks.com", "tlf": 688641357},
    {"id": 2, "cif": 987654321, "razon": "Planeta", "web": "https://planeta.com", "correo": "info@planeta.com",
     "tlf": 688641257}
]

@editoriales_bp.get('/editoriales')
def get_editoriales():
    return jsonify(editoriales)


@editoriales_bp.get('/editoriales/<int:id>')
def get_editorial(id):
    for n in editoriales:
        if n['id'] == id:
            return jsonify(n)

    return jsonify({'error': 'not found'})

@editoriales_bp.post('/editoriales')
def add_editorial():
    if request.is_json:
        editorial_json = request.get_json()
        editorial = Editorial(id=editorial_json['id'], cif=editorial_json['cif'], razon=editorial_json['razon'],
                              direccion=editorial_json['direccion'], web=editorial_json['web'],
                              correo=editorial_json['correo'], tlf=editorial_json['tlf'])
        editoriales.append(editorial.serialize())
        return editorial.serialize(), 201
    else:
        return '{error: "JSON invalido"}', 501


@editoriales_bp.put('/editoriales/<int:id>')
@editoriales_bp.patch('/editoriales/<int:id>')
def modify_editorial(id):
    if request.is_json:
        editorial_json = request.get_json()
        for editorial in editoriales:
            if editorial['id'] == id:
                for element in editorial_json:
                    editorial[element] = editorial_json[element]
                return editorial_json, 200
    else:
        return {"error": "JSON invalido"}

@editoriales_bp.delete('/editoriales/<int:id>')
def delete_editorial(id):
    for editorial in editoriales:
        if editorial['id'] == id:
            editoriales.remove(editorial)
            return editorial, 200