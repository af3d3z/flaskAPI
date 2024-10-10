from flask import *
from models.Editorial import Editorial

editoriales = [
    {"id":1, "cif":123456789, "razon":"Manolo Books", "web":"https://manolobooks.com", "correo": "info@manolobooks.com", "tlf": 688641357},
    {"id":2, "cif":987654321, "razon":"Planeta", "web":"https://planeta.com", "correo": "info@planeta.com", "tlf": 688641257}
]

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!'

@app.get('/editoriales')
def get_editoriales():
    return jsonify(editoriales)

@app.get('/editoriales/<int:id>')
def get_editorial(id):
    for n in editoriales:
        if n['id'] == id:
            return jsonify(n)

    return jsonify({'error':'not found'})

@app.post('/editoriales')
def add_editorial():
    if request.is_json:
        editorial_json = request.get_json()
        editorial = Editorial(id=editorial_json['id'], cif=editorial_json['cif'], razon=editorial_json['razon'], direccion=editorial_json['direccion'], web=editorial_json['web'], correo=editorial_json['correo'], tlf=editorial_json['tlf'])
        editoriales.append(editorial.serialize())
        return editorial.serialize(),201
    else:
        return '{error: "JSON invalido"}', 501

@app.put('/editoriales/<int>:id')
@app.patch('/editoriales/<int>:id')
def modify_editorial(id):
    if request.is_json:
        editorial_json = request.get_json()
        new_editorial = Editorial(id=editorial_json['id'], cif=editorial_json['cif'], razon=editorial_json['razon'], direccion=editorial_json['direccion'], web=editorial_json['web'], correo=editorial_json['correo'], tlf=editorial_json['tlf'])
        for editorial in editoriales:
            if editorial['id'] == id:
                for element in new_editorial:
                    editorial[element] = new_editorial[element]
                return jsonify(new_editorial.serialize())

    else:
        return {"error": "JSON invalido"}
        

        
        

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5050")