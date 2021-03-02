from flask_restful import Resource
from flask import request
from werkzeug.security import safe_str_cmp

from flask_jwt_extended import create_access_token, create_refresh_token
from models.user import UserModel
from schemas.user import UserSchema

userSchema = UserSchema()


class UserRegister(Resource):
    @classmethod
    def post(cls):
        user_json=request.get_json()
        user = userSchema.load(user_json)

        if UserModel.find_by_username(user.username):
            return {"message": "username already exists"},400
        
        user.save_to_db()
        return {"message":"User Registered"},201



class User(Resource):
    @classmethod
    def get(cls,user_id:int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message":"user not found"},404
        return userSchema.dump(user),200

        

    @classmethod
    def delete(cls,user_id:int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": "User not found"},404

        user.delete_from_db()
        return {"message":"User deleted"},200

class UserLogin(Resource):
    @classmethod
    def post(cls,):
        user_json = request.get_json()
        user_data = userSchema.load(user_json)

        user = UserModel.find_by_username(user_data.username)

        if user and safe_str_cmp(user_data.password,user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        return {"message": gettext("user_invalid_credentials")}, 401
