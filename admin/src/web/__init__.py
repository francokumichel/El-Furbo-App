from flask import Flask, render_template
from os import urandom
from src.web.config import config


def create_app(env="development", static_folder="../../static"):

    app = Flask(__name__, static_folder=static_folder)

    # Configuro el entorno
    app.secret_key = urandom(24)
    app.config.from_object(config[env])

    @app.get("/")
    def entry_point():
        return render_template("home.html")

    return app