from flask import Flask
from app.config import Config
from app.database import mongo

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)

    from app.routes import user_bp
    app.register_blueprint(user_bp)

    return app
