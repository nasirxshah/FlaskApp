from bson import ObjectId
from flask import request
from flask_restful import Resource
from werkzeug.security import generate_password_hash

from app.extensions import mongo


class UserList(Resource):
    def get(self):
        users = mongo.db.users.find(projection={"name":1,"email":1,"username":1})
        response = []
        for user in users:
            response.append({
                "id":str(user['_id']),
                "username": user['username'],
                "name": user['name'],
                "email": user['email']
            })
        return response

    def post(self):
        password = request.json['password']

        hashed_password = generate_password_hash(password)

        id = mongo.db.users.insert_one({
            'name':request.json['name'],
            'email': request.json['email'],
            'username':request.json['username'],
            'password':hashed_password
        }).inserted_id

        return {"id":str(id)}, 201


class UserDetail(Resource):
    def get(self, id):
        user = mongo.db.users.find_one({"_id":ObjectId(id)},projection={"name":1,"email":1,"username":1})
        return {
                "id":str(user['_id']),
                "username": user['username'],
                "name": user['name'],
                "email": user['email']
            }

    def put(self,id):
        password = request.json['password']
        hashed_password = generate_password_hash(password)

        mongo.db.users.update_one({'_id':ObjectId(id)},{"$set":{
            'name':request.json['name'],
            'email': request.json['email'],
            'username':request.json['username'],
            'password':hashed_password
        }})
        return {"id":id}
    
    def delete(self, id):
        mongo.db.users.delete_one({"_id":ObjectId(id)})
        return "",204