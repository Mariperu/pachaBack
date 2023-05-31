# config/dev.py

from .default import *

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost:5432/minimarkett'