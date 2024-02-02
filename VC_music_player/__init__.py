from flask import Flask
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
import os

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    Bootstrap5(app)
    return app
