from ma import ma
from marshmallow import fields
from models.product import ProductModel

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel
        load_only=("shop_id","product_id")
        dump_only = ("mrp","sale_price","product_name","discount",)        
        load_instance = True
        include_fk = False

class ProductDetailsSchema(ma.SQLAlchemySchema):

    class Meta:
            model = ProductModel

    product_name = ma.auto_field()
    sale_price = ma.auto_field()
    mrp = ma.auto_field()
    discount = fields.Float()
