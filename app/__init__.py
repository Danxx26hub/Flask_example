from flask import Flask
from app.config import get_settings


app = Flask(__name__, instance_relative_config=True)
app_settings = get_settings()
app.config.from_object(app_settings())


from app import views
