from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_s3 import FlaskS3

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
app.config['S3_BUCKET_NAME'] = 'grampy101'
s3 = FlaskS3(app)

from app import views, models