# ruff: noqa: F401
from .auth import auth_blueprint
from .main import main_blueprint
from .user import bp as user_blueprint
from .application import application_bp as application_blueprint
from .multilingual import multilingual
from .admin import admin_blueprint
from .cookie_policy import cookie_policy_bp as cookie_policy_blueprint
