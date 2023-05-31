# config/default.py

from os.path import abspath, dirname, join


# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))
# Media dir
MEDIA_DIR = join(BASE_DIR, 'media')
POSTS_IMAGES_DIR = join(MEDIA_DIR, 'posts')

SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
ITEMS_PER_PAGE = 5
# Database configuration
SQLALCHEMY_TRACK_MODIFICATIONS = False

# App environments
APP_ENV_LOCAL = 'local'
APP_ENV_TESTING = 'testing'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''

MAIL_SERVER = ' '
MAIL_PORT = 00
MAIL_USERNAME = ' '
MAIL_PASSWORD = ' '
DONT_REPLY_FROM_EMAIL = ' '
ADMINS = (' ', )
MAIL_USE_TLS = True
MAIL_DEBUG = True