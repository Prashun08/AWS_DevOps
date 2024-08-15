from flask import Config, Flask
from flask_session import Session
from redis import Redis
from app import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Redis connection
    redis_client = Redis.from_url(app.config['REDIS_URL'])

    # Setup session with Redis
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_USE_SIGNER'] = True
    app.config['SESSION_REDIS'] = redis_client

    Session(app)

    # Import and register blueprints (routes)
    from app import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

