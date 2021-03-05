from ma import ma
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from models.shop import ShopModel

class ShopSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ShopModel        
        dump_only=("id","shop_id","active")
        load_instance = True