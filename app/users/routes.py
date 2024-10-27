import json

import bcrypt
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token

from datos import leer_fichero, escribir_fichero

ficheroUsers = "app/users/data.json"

users_bp = Blueprint('users_bp', __name__)

@users_bp.post('/login')
def login_users():
    users = leer_fichero(ficheroUsers)
    if request.is_json:
        user = request.get_json()
        username = user['username']
        password = user['password'].encode('utf-8')

        for u in users:
            if u['username'] == username:
                passFile = u['password']
                if bcrypt.checkpw(password, bytes.fromhex(passFile)):
                    token = create_access_token(identity=username)
                    return {'token': token}, 200
                else:
                    return {'error': 'Credenciales inválidas.'}, 401
        return {'error': 'Usuario no encontrado.'}, 404
    return {'error': 'Request must be JSON'}, 415

@users_bp.post('/')
def register_user():
    if request.is_json:
        user = request.get_json()
        password = user['password'].encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password, salt).hex()
        user['password'] = hashed
        users = leer_fichero(ficheroUsers)
        users.append(user)
        escribir_fichero(ficheroUsers, users)

        token = create_access_token(identity=user['username'])
        return {'token': token}, 201
    return {"error": "Must be JSON."}, 415