from flask import Flask, current_app
from app.config import get_settings
from flask_caching import Cache
from flask_admin import Admin



# set optional bootswatch theme



app = Flask(__name__, instance_relative_config=True)
app_settings = get_settings('dev')

app.config.from_object(app_settings('dev'))
cache = Cache(app)

app.logger.info("app started")
print(app.config)



admin = Admin(app, name='microblog', template_mode='bootstrap3')

from app import views, appAdmin
