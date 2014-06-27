from flask_assets import Environment, Bundle

CSS_ASSETS = [
    Bundle('css/application.scss', filters='pyscss', output='css/compiled-scss.css')
]

JS_ASSETS = [
    'js/centered.js'
]

def register_assets(app):
    assets = Environment(app)
    assets.debug = app.debug
    assets.auto_build = True
    assets.url = app.static_url_path

    css_all = Bundle(*CSS_ASSETS, filters='cssmin', output='css/bundle.min.css')
    js_all = Bundle(*JS_ASSETS, filters='rjsmin', output='js/all.min.js')

    assets.register('css_all', css_all)
    assets.register('js_all', js_all)
    app.logger.info("Registered assets...")
    return assets
