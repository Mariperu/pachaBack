# config/dev.py

from .default import *

from dotenv import load_dotenv
import os

load_dotenv()
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]

DEBUG = True
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://postgres:{POSTGRES_PASSWORD}@localhost:5432/miniblog"
)

