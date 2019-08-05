import os

class Config:
    """
    This is the parent class which will have the general configurations
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = "app/static/photos"




class ProdConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL')
    

class DevConfig(Config):
    SECRET_KEY='absc'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:vinceobindi1005@localhost/thinkout'
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}

