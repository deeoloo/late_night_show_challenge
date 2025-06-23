from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.config import Config
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

# Initialize extensions first (without app)
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Import models AFTER db initialization
    from server.models import user, guest, episode, appearance

    # Import controllers AFTER all extensions are ready
    from server.controllers.auth_controller import auth_bp
    from server.controllers.episode_controller import episode_bp
    from server.controllers.guest_controller import guest_bp
    from server.controllers.appearance_controller import appearance_bp

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(appearance_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)