import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY', '.!?Pc$%pC')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:password@postgres:5432/postgres')
