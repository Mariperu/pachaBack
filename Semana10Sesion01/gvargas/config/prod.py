# config/prod.py

from .default import *

SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@prod_host:port/db_name'
