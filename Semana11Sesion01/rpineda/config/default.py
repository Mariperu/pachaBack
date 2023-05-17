# config/default.py

from os.path import abspath, dirname


# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))

SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

# Database configuration
SQLALCHEMY_TRACK_MODIFICATIONS = False

# App environments
APP_ENV_LOCAL = 'local'
APP_ENV_TESTING = 'testing'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USERNAME = 'rpinedaec93@gmail.com'
MAIL_PASSWORD = 'asdasdasda'
DONT_REPLY_FROM_EMAIL = 'miniblog@x-codec.net'
ADMINS = ('rpineda@x-codec.net', )
MAIL_USE_TLS = True
MAIL_DEBUG = False