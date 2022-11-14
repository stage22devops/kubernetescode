from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Update 14/11/2022'
