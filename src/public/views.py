from flask import Blueprint, render_template

blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def welcome():
    return render_template("public/welcome.tmpl")
