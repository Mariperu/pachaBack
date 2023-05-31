# entrypoint.py

import os

from app import create_app


settings_module = os.getenv('APP_SETTINGS_MODULE')
print(settings_module)
app = create_app()