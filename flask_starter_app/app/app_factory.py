from flask import Flask
from injector import Injector
from flask_injector import FlaskInjector

from .app_injector import configure
from .views.test_view import bp as main_blueprint

class AppFactory:
    def create_app(self):
        app = Flask(__name__)
        self._register_blueprints(app)
        self._configure_dependencies(app) # shgould be called after routes are added(Ex. @app.route('/')
        return app

    def _register_blueprints(self, app):        
        app.register_blueprint(main_blueprint)
        
    def _configure_dependencies(self, app):
       FlaskInjector(app=app, modules=[configure])

