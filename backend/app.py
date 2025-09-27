from flask import Flask
from config import Config
from extensions import db, migrate
from routes import bp as api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api_bp)

    @app.route("/")
    def index():
        return "MTAA Assistant Backend - healthy"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(__import__("os").environ.get("PORT", 5000)))
