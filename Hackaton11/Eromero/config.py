from orator import DatabaseManager, Schema
import psycopg2

class OratorConfig:
    ORATOR_DATABASES = {
        'postgres': {
            'driver': 'postgres',
            'host': 'localhost',
            'database': 'market',
            'user': 'patron',
            'password': 'Papa1234',
            'prefix': ''
        }
    }
    SECRET_KEY = "ANAMA23"


db = DatabaseManager(OratorConfig.ORATOR_DATABASES)
schema = Schema(db)

