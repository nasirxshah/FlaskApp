from flask_restful import Api
from .views import UserList, UserDetail

api = Api()
api.add_resource(UserList,"/users/")
api.add_resource(UserDetail, "/users/<string:id>")