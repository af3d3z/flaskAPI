import pymssql
import requests
from flask import *

from models.Editorial import Editorial


app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 763120},
    {"id": 3, "name": "Egipt", "capital": "Cairo", "area": 1010408},
]

@app.route('/')
def index():
    return 'Hello world'

@app.get('/countries')
def get_countries():
    return jsonify(countries)

@app.get('/countries/<int:id>')
def get_country(id):
    for country in countries:
        if country['id'] == id:
            return jsonify(country)

@app.post('/countries')
def add_country():
    if request.is_json:
        country = request.get_json()
        country['id'] = len(countries) + 1
        countries.append(country)

        return country, 201
    else:
        return {"error": "Request must be JSON"}, 415


@app.put('/countries/<int:id>')
@app.patch('/countries/<int:id>')
def modify_country(id):
    if request.is_json:
        new_country = request.get_json()
        for country in countries:
            if country['id'] == id:
                for element in new_country:
                    country[element] = new_country[element]
                return new_country, 200
    return {"error": "Request must be JSON"}, 415

@app.delete('/countries/<int:id>')
def delete_country(id):
    for country in countries:
        if country['id'] == id:
            countries.remove(country)
            return "{}", 200
    return {"error": "Country not found"}, 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
