from flask import Flask
from app.models import db
#from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Imports models after db initialization to avoid circular imports
    from app.models import Hero, Power, HeroPower

    # Imports and registers blueprints
    from app.routes import api
    app.register_blueprint(api)

    return app
