from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_main_app(config_name):
    app = Flask(__name__,instance_relative_config = True)

    app.config.from_object(config_options[config_name]) #creating app configura
    bootstrap.init_app(app)#init flask extension

    from .main import main as main_blueprint#registr blueprint
    app.register_blueprint(main_blueprint)

    from .requests import configure_request#setting config
    configure_request(app)

    return app