from flask import Blueprint, render_template

blueprint = Blueprint('iphone', __name__)

@blueprint.route('/', methods=['GET'])
def root():
    return render_template("iphone/root.tmpl")

@blueprint.route('/index', methods=['GET'])
def index():
    return render_template("iphone/index.tmpl")

@blueprint.route('/about', methods=['GET'])
def about():
    return render_template("iphone/about.tmpl")

@blueprint.route('/blog', methods=['GET'])
def blog():
    return render_template("iphone/blog.tmpl")

@blueprint.route('/consulting', methods=['GET'])
def consulting():
    return render_template("iphone/consulting.tmpl")

@blueprint.route('/on-call', methods=['GET'])
def on_call():
    return render_template("iphone/on-call.tmpl")

@blueprint.route('/development', methods=['GET'])
def development():
    return render_template("iphone/development.tmpl")
