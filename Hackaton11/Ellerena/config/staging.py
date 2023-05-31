# config/staging.py

from .default import *


APP_ENV = APP_ENV_STAGING

SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@host:port/db_name'