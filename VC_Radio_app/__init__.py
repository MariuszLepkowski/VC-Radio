from flask import Flask
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
import os
from VC_Radio_app.views.main_panel import main_panel_blueprint

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_panel_blueprint)
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    Bootstrap5(app)
    return app
