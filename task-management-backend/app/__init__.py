from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Task%20Management_owner:ZR0us8TaDzxo@ep-royal-bonus-a1zgovop.ap-southeast-1.aws.neon.tech/Task%20Management?sslmode=require'
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

    return app
