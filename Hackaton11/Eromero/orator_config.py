from orator import DatabaseManager, Schema

DATABASES = {
    'default': 'postgres',
    'postgres': {
        'driver': 'postgres',
        'host': 'localhost',
        'database': 'market',
        'user': 'patron',
        'password': 'Papa1234',
        'prefix': ''
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
