from flask import Blueprint, render_template

blueprint = Blueprint('iphone', __name__)

@blueprint.route('/iphone', methods=['GET'])
def dashboard():
    return render_template("iphone/dashboard.tmpl")
