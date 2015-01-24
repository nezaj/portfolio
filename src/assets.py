from flask_assets import Environment, Bundle

VENDOR_ASSETS = ['css/vendor/tipsy.css']

JS_ASSETS = [
    'js/vendor/jquery.js',
    'js/vendor/tipsy.js',
    'js/application.js'
]

def register_assets(app):
    assets = Environment(app)
    assets.debug = app.debug
    assets.auto_build = True
    assets.url = app.static_url_path

    css_vendor = Bundle(*VENDOR_ASSETS, filters='cssmin',
                        output='css/vendor.compiled.css')
    css_welcome = Bundle('css/welcome.scss', filters='pyscss',
                         output='css/welcome.compiled.css')

    js_all = Bundle(*JS_ASSETS, filters='rjsmin', output='js/all.min.js')

    assets.register('css_vendor', css_vendor)
    assets.register('css_welcome', css_welcome)
    assets.register('js_all', js_all)
    app.logger.info("Registered assets...")

    return assets
