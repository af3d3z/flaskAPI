from flask import Flask

from app.editoriales.routes import editoriales_bp
from app.libros.routes import libros_bp

app = Flask(__name__)

@app.get('/')
def index():
    return "Hello world!"

app.register_blueprint(editoriales_bp, url_prefix='/editoriales')
app.register_blueprint(libros_bp, url_prefix='/libros')