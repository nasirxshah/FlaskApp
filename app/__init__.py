from flask import Flask
from .api import api
from .api.mongo import mongo

app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/test"

mongo.init_app(app)
api.init_app(app)