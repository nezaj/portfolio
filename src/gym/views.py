from flask import Blueprint, render_template

blueprint = Blueprint('gym', __name__)

@blueprint.route('/', methods=['GET'])
def root():
    return render_template("gym/root.tmpl")
