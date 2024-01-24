## IMPORT FLASK MODULE + EXTENSIONS
from flask import Flask, jsonify, render_template

## IMPORT CONFIG
from src.config import ApplicationConfig

## INSTANTIATE FLASK APPLICATION
def create_app():

    ## INSTANTIATE FLASK APP
    app = Flask(__name__)

    ## LOAD APPLICATION CONFIG
    app.config.from_object(ApplicationConfig)

    ## IMPORT ROUTES
    from src.routes import route_bp
    app.register_blueprint(route_bp)
            
    return app