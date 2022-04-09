from flask import Flask 

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'HHEldkj 033rk ldk 0lkle'
    return app 