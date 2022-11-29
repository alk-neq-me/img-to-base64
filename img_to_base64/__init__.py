import os
from dotenv import load_dotenv
from flask import Flask


load_dotenv()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from .routes import views
    app.register_blueprint(views.blue_print)

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    return app
