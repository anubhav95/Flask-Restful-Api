from ma import ma
from marshmallow_sqlalchemy import ModelSchema
from models.user import UserModel

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_only=("password",)
        dump_only=("id",)