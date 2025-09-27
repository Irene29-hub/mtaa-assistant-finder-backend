import os

class Config:
    DEBUG = os.getenv("FLASK_ENV", "production") == "development"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or "sqlite:///dev.db"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret")
