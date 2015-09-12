from flask_assets import Environment, Bundle

INDEX_ASSETS = [
    'css/vendor/tipsy.css',
    Bundle('css/welcome.scss', filters='pyscss', output='css/compiled-scss.css')
]

BLOG_ASSETS = [
    'css/vendor/tipsy.css',
    'css/vendor/readable-bootstrap.css',
    Bundle('css/blog.scss', filters='pyscss', output='css/compiled-scss.css')
]

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

    css_blog = Bundle(*BLOG_ASSETS, filters='cssmin', output='css/blog.min.css')
    css_welcome = Bundle(*INDEX_ASSETS, filters='cssmin', output='css/welcome.min.css')

    js_all = Bundle(*JS_ASSETS, filters='rjsmin', output='js/all.min.js')

    assets.register('css_blog', css_blog)
    assets.register('css_welcome', css_welcome)
    assets.register('js_all', js_all)
    app.logger.info("Registered assets...")

    return assets
