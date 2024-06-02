import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('https://cloud.mongodb.com/v2/665b4925bdea6c1a9e6a298c#', 'thanaal20220062:MT020605')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')
