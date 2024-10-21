from flask import Flask
from flask_jwt_extended import JWTManager

from app.editoriales.routes import editoriales_bp
from app.libros.routes import libros_bp
from app.users.routes import users_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave'
jwt = JWTManager(app)

@app.get('/')
def index():
    return "Hello world!"

app.register_blueprint(editoriales_bp, url_prefix='/editoriales')
app.register_blueprint(libros_bp, url_prefix='/libros')
app.register_blueprint(users_bp, url_prefix='/users')