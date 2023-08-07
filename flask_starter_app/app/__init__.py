from app.app_factory import AppFactory

def create_app():
    app_factory = AppFactory()
    app = app_factory.create_app()
    return app
