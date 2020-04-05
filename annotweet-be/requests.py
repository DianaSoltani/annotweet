from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'my name jeff'

@app.route('/test/')
def test():
    return {'test': 'yeet'}