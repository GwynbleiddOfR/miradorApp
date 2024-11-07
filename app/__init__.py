from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SingletonDB:
    _instance = None

    def __new__(cls, app=None):
        if cls._instance is None:
            cls._instance = super(SingletonDB, cls).__new__(cls)
            cls._instance.init_app(app)
        return cls._instance

    def init_app(self, app):
        if app is not None:
            db.init_app(app)

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    SingletonDB(app)  # Singleton instance of DB

    with app.app_context():
        from models import DepartamentoModel, GastoComunModel
        try:
            db.create_all()
            print("Base de datos creada exitosamente")
        except Exception as e:
            print(f"Error al crear la base de datos: {e}")

    return app