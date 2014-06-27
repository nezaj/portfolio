from flask import redirect, url_for

def register_error_handlers(app):
    def handler(err):  # pylint: disable=W0613
        return redirect(url_for("main.welcome"))
    return app.errorhandler(404)(handler)
