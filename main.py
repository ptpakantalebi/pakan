from flask import Flask
app = Flask(__name__)
@app.route("/<name>")
def hello_world(name):
    return f'{name} welcome to this website, I hope you like it'
