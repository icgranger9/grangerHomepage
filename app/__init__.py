from flask import Flask
from app.main import bp as main_bp
# from config import Config

def create_app(config_class=None):
    app = Flask(__name__)
    # app.config.from_object(config_class)

    # Initialize Flask extensions here


    # Register blueprints here
    app.register_blueprint(main_bp)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app