from flask import *
from models.Editorial import Editorial
from models.Libro import Libro

editoriales = [
    {"id": 1, "cif": 123456789, "razon": "Manolo Books", "web": "https://manolobooks.com",
     "correo": "info@manolobooks.com", "tlf": 688641357},
    {"id": 2, "cif": 987654321, "razon": "Planeta", "web": "https://planeta.com", "correo": "info@planeta.com",
     "tlf": 688641257}
]

libros = [
    {"id": 1, "precio": 15, "isbn": "978-7-2398-8924-8", "titulo": "Black Hat Go", "numpag": 345, "tematica": "Tecnología", "id_editorial": 1},
    {"id": 2, "precio": 20, "isbn": "968-3-2338-6783-0", "titulo": "Python deep learning", "numpag": 234, "tematica": "Tecnología", "id_editorial": 2}
]

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Flask!'


@app.get('/editoriales')
def get_editoriales():
    return jsonify(editoriales)

@app.get('/libros')
def get_libros():
    return jsonify(libros)

@app.get('/editoriales/<int:id>')
def get_editorial(id):
    for n in editoriales:
        if n['id'] == id:
            return jsonify(n)

    return jsonify({'error': 'not found'})

@app.get('/libros/<int:id>')
def get_libro(id):
    for n in libros:
        if n['id'] == id:
            return jsonify(n)

    return jsonify({'error': 'not found'})


@app.post('/editoriales')
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

@app.post('/libros')
def add_libro():
    if request.is_json:
        libro_json = request.get_json()
        libro = Libro(id=libro_json['id'], precio=libro_json['precio'], isbn=libro_json['isbn'],
                      titulo=libro_json['titulo'], numpag=libro_json['numpag'], tematica=libro_json['tematica'], id_editorial=libro_json['id_editorial'])
        libros.append(libro.serialize())
        return libro.serialize(), 201
    else:
        return '{error: "JSON invalido"}', 501



@app.put('/editoriales/<int:id>')
@app.patch('/editoriales/<int:id>')
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

@app.put('/libros/<int:id>')
@app.patch('/libros/<int:id>')
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

@app.delete('/editoriales/<int:id>')
def delete_editorial(id):
    for editorial in editoriales:
        if editorial['id'] == id:
            editoriales.remove(editorial)
            return editorial, 200

@app.delete('/libros/<int:id>')
def delete_libro(id):
    for libro in libros:
        if libro['id'] == id:
            libros.remove(libro)
            return libro, 200



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5050)
