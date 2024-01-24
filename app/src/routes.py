## IMPORT REQUIRED MODULES
from flask import render_template, Blueprint
route_bp = Blueprint('route_blueprint', __name__)

## ROUTE: HOME PAGE
@route_bp.route("/", methods=['GET'])
@route_bp.route("/index", methods=['GET'])
def index_page():

    ## RETURN HOME PAGE
    return render_template('index.html', title="TailwindCSS + Flask Demo", page="index")

## ROUTE: SETTINGS PAGE
@route_bp.route("/settings", methods=['GET'])
def settings_page():

    ## RETURN HOME PAGE
    return render_template('index.html', title="TailwindCSS + Flask Demo", page="settings")

## ROUTE: SYSTEM PAGE
@route_bp.route("/system", methods=['GET'])
def system_page():

    ## RETURN HOME PAGE
    return render_template('system.html', title="TailwindCSS + Flask Demo", page="system")