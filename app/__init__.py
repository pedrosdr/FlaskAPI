from flask import Flask
from flask_restful import Api
import psycopg2 as pg

app = Flask(__name__)
api = Api(app)
conn_string = "host='localhost' dbname='FlaskAPI' user='postgres' password='secret'"
db = pg.connect(conn_string)

from app.controllers import video_controller