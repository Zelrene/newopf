from markupsafe import escape
from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def hello():
	return '<h1>Hello, World!</h1>'
