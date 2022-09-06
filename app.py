from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi, we have finished the deployment using the ArgoCD method !!!!'
