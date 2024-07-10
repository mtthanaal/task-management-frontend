import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://Task%20Management_owner:ZR0us8TaDzxo@ep-royal-bonus-a1zgovop.ap-southeast-1.aws.neon.tech/Task%20Management?sslmode=require')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')
