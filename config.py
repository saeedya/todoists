import os

# Generate a random secret key
secret_key = os.urandom(24).hex()

class Config:
    SECRET_KEY = secret_key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///todo.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False