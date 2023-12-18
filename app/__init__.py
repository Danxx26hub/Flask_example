from flask import Flask
from app.config import get_settings


app = Flask(__name__, instance_relative_config=True)
app_settings = get_settings('dev')
print(app_settings('dev').env)
app.config.from_object(app_settings('dev'))
print(app.config)

from app import views
