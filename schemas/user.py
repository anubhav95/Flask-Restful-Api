from ma import ma
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from models.user import UserModel

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_only=("password",)
        dump_only=("id",)
        load_instance = True


class UserLoginSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel
        load_instance = True
    username = fields.Str()
    password = fields.Str()
    
    
