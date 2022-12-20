from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, from xx-flask-demo-3!!'

@app.route('/')
def hello_root():
    return 'Hello! from xx-flask-demo-3!!'