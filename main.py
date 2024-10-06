import pymssql
from flask import *

from models.Editorial import Editorial


def db_init():
    return pymssql.connect(
        server='IdeaPad3Slim',
        user='alebozek',
        password='EjercicioAPI',
        database='EjercicioAPI'
    )

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world'

@app.get('/api/editoriales')
def get_editoriales():
    editoriales = []
    cursor.execute('SELECT * FROM EDITORIAL')
    for row in cursor:
        editorial = Editorial(id=row['Id'], cif=row['CIF'], direccion=row['Direccion'], razon=row['RazonSocial'],
                              web=row['Web'], correo=row['Correo'], tlf=row['Telefono'])
        editoriales.append(editorial)
    return jsonify(editoriales)



if __name__ == '__main__':
    cursor = db_init().cursor()
    app.run(debug=True, host='0.0.0.0', port=5000)
