from .default import *

from dotenv import load_dotenv
import os

load_dotenv()

TESTING = True
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root0709@localhost:5432/sv005618467'
