from flask_restful import Resource
from flask import request
from werkzeug.security import safe_str_cmp

from flask_jwt_extended import create_access_token, create_refresh_token,jwt_required
from models.product import ProductModel
from schemas.product import ProductSchema,ProductDetailsSchema

product_schema = ProductSchema()
product_details_schema = ProductDetailsSchema()



class ProductRes(Resource):
    @classmethod
    @jwt_required()
    def post(cls):        
        product_json = request.get_json()        
        product_data = product_schema.load(product_json)        
        product = ProductModel.get_product_by_id(product_data.product_id)
        
        if product:
            product.product_name=product.product_name.rstrip()      
            discount = ((product.mrp - product.sale_price)/100)*100
            product.discount = discount            
            return product_details_schema.dump(product),200
                           
        return {"message":"Cannot find product"},404

