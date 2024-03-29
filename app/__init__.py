from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_migrate import Migrate


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
migrate = Migrate()

photos = UploadSet('photos',IMAGES)




def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://moringa:vinceobindi1005@localhost/thinkout'

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    
    # configure_uploads(app,photos)
    configure_uploads(app,photos)


    return app




