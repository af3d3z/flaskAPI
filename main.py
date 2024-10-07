import pymssql
from flask import *

from models.Editorial import Editorial


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
