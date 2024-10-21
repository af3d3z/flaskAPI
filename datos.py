from flask import json

def leer_fichero(fichero: str):
    with open(fichero, 'r') as f:
        dic = json.load(f)
        f.close()
        return dic

def escribir_fichero(fichero:str, datos):
    with open(fichero, 'w') as f:
        json.dump(datos, f)
        f.close()