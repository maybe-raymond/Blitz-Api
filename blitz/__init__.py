from flask import Flask
from flask_restful import Api
from blitz.config import Production
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from blitz.Celery_config import make_celery


app = Flask(__name__)
app.config.from_object(Production())
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)


celery = make_celery(app)
api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)


from blitz import routes
