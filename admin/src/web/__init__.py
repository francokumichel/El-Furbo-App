from flask import Flask, render_template
from os import urandom
from src.web.config import config
from src.core import database, seeds
from src.web.controllers.user import users_blueprint


def create_app(env="development", static_folder="../../static"):

    app = Flask(__name__, static_folder=static_folder)

    # Configuro el entorno
    app.secret_key = urandom(24)
    app.config.from_object(config[env])

    # Inicializo la base de datos
    database.init_app(app)

    # Registramos las rutas con blueprint
    app.register_blueprint(users_blueprint)


    @app.get("/")
    def entry_point():
        return render_template("home.html")
    
    @app.cli.command(name="resetdb")
    def resetdb():
        '''
            Función para reiniciar la base de datos. La forma de llamar a esta funcionalidad es mediante el
            comando "flask resetdb"
        '''
        database.reset_db()
    
    @app.cli.command(name="seedsdb")
    def seedsdb():
        '''
            Función para cargar la bd con datos genéricos. La forma de llamar a esta funcionalidad es mediante el
            comando "flask seedsdb"
        '''
        seeds.run()


    return app