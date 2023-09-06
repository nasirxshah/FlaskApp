from flask import Blueprint
from flask_restful import Api

from app.api.resources.user import UserDetail, UserList

api_bp = Blueprint('api',__name__)
api = Api(api_bp)

api.add_resource(UserList,"/users/")
api.add_resource(UserDetail, "/users/<string:id>")
