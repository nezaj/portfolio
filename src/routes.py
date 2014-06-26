from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def welcome():
    return render_template("welcome.tmpl")
