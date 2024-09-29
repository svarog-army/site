import os

from flask import Flask, render_template, request, g, redirect, url_for
from flask_login import LoginManager
from werkzeug.exceptions import HTTPException
from flask_migrate import Migrate
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from flask_babel import Babel

from config import TRANSLATIONS_DIR, CFG
from svarog.logger import log
from .database import db

# instantiate extensions
login_manager = LoginManager()
migration = Migrate()
mail = Mail()
csrf = CSRFProtect()
babel = Babel()


def create_app(environment="development"):
    from config import config
    from svarog.views import (
        main_blueprint,
        auth_blueprint,
        user_blueprint,
        multilingual,
        application_blueprint,
    )
    from svarog import models as m

    # Instantiate app.
    app = Flask(__name__)

    # Set app config.
    env = os.environ.get("APP_ENV", environment)
    configuration = config(env)
    assert not configuration.IS_API
    app.config.from_object(configuration)
    configuration.configure(app)
    log(log.INFO, "Configuration: [%s]", configuration.ENV)

    # Set up extensions.
    db.init_app(app)
    migration.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)

    def get_locale():
        # Get locale from URL.
        if not g.get("lang_code", None):
            g.lang_code = (
                request.accept_languages.best_match(CFG.BABEL_SUPPORTED_LOCALES)
                or CFG.BABEL_DEFAULT_LOCALE
            )
        return g.lang_code

    babel.init_app(
        app,
        default_locale=CFG.BABEL_DEFAULT_LOCALE,
        locale_selector=get_locale,
        default_translation_directories=TRANSLATIONS_DIR,
    )

    # Register blueprints.
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(application_blueprint)
    app.register_blueprint(multilingual)

    @app.route("/")
    def home():
        if not g.get("lang_code", None):
            get_locale()
        return redirect(url_for("multilingual.index"))

    # Set up flask login.
    @login_manager.user_loader
    def get_user(id: int):
        query = m.User.select().where(m.User.id == int(id))
        return db.session.scalar(query)

    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"
    login_manager.anonymous_user = m.AnonymousUser

    # Error handlers.
    @app.errorhandler(HTTPException)
    def handle_http_error(exc):
        return render_template("error.html", error=exc), exc.code

    return app
