from flask import *
import pymssql
from models.Editorial import Editorial

conn = pymssql.connect(
    server='warmachine',
    user='alebozek',
    password='EjercicioAPI',
    database='EjercicioAPI'
)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!'

@app.get('/editoriales')
def get_editoriales():
    editoriales = []
    cursor.execute("SELECT * FROM EDITORIAL")
    results = cursor.fetchall()
    for r in results:
        editorial = Editorial(id=r['Id'], cif=r['CIF'], razon=r['RazonSocial'], direccion=r['Direccion'], web=r['Web'], correo=r['Correo'], tlf=r['Telefono'])
        editoriales.append(editorial.serialize())
    return jsonify(editoriales)

@app.post('/editoriales')
def add_editorial():
    if request.is_json:
        editorial_json = request.get_json()
        editorial = Editorial(id=editorial_json['id'], cif=editorial_json['cif'], razon=editorial_json['razon'], direccion=editorial_json['direccion'], web=editorial_json['web'], correo=editorial_json['correo'], tlf=editorial_json['tlf'])
        print(f"INSERT INTO EDITORIAL VALUES ({editorial.id}, {editorial.cif}, {editorial.razon}, {editorial.direccion}, {editorial.web}, {editorial.correo}, {editorial.tlf})")
        cursor.execute(f"INSERT INTO EDITORIAL VALUES ({editorial.id}, {editorial.cif}, '{editorial.razon}', '{editorial.direccion}', '{editorial.web}', '{editorial.correo}', '{editorial.tlf}')")
        return '{"msg": "El recurso ha sido creado."}',201
    else:
        return '{error: "JSON invalido"}', 501

@app.put('/editoriales')
@app.patch('/editoriales')
def modify_editorial():
    if request.is_json:
        editorial_json = request.get_json()
        new_editorial = Editorial(id=editorial_json['id'], cif=editorial_json['cif'], razon=editorial_json['razon'], direccion=editorial_json['direccion'], web=editorial_json['web'], correo=editorial_json['correo'], tlf=editorial_json['tlf'])
        print(new_editorial)
        cursor.execute(f"SELECT COUNT(1) FROM EDITORIAL WHERE ID = {new_editorial.id}")
        result = cursor.fetchall()[0][0]
        print(result)
        if result == 1:
            return "bomba"
        else:
            return {"error": "La editorial no existe."}  
    else:
        return {"error": "JSON invalido"}
        
        
        
        

if __name__ == '__main__':
    cursor = conn.cursor()
    app.run(debug=True, host="0.0.0.0", port="5050")