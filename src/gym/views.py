from flask import Blueprint, render_template

blueprint = Blueprint('gym', __name__)

@blueprint.route('/gym', methods=['GET'])
def dashboard():
    return render_template("gym.tmpl")
