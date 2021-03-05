from flask_restful import Resource
from flask import request
from werkzeug.security import safe_str_cmp

from flask_jwt_extended import create_access_token, create_refresh_token,jwt_required
from models.shop import ShopModel
from schemas.shop import ShopSchema

shop_schema = ShopSchema()

class ShopRes(Resource):
    @classmethod
    def get(cls):
        shops = ShopModel.get_all_shops()
        return [shop_schema.dump(shop) for shop in shops]

    @classmethod
    def post(cls):        
        shop_json = request.get_json()
        shop = shop_schema.load(shop_json)        
        shop.active=True
        shop.save_to_db()
        return {"message":"Shop Created"},201

