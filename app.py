import os

from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from marshmallow import ValidationError
from ma import ma
from db import db

from resources.user import UserRegister,User,UserLogin
from resources.product import ProductRes
from resources.shop import ShopRes


app = Flask(__name__)
app.config["Debug"]=True
app.config["SQLALCHEMY_DATABASE_URI"]="################"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["PROPAGATE_EXCEPTIONS"]=True

app.secret_key="Anubhav"
api = Api(app)
jwt = JWTManager(app)

migrate = Migrate(app,db)

db.init_app(app)
ma.init_app(app)

@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400

api.add_resource(UserRegister, "/register")
api.add_resource(User, "/user/<int:user_id>")
api.add_resource(UserLogin, "/login")
api.add_resource(ProductRes, "/product")
api.add_resource(ShopRes, "/shop")









if __name__ == "__main__":
    
    app.run(port=5000, debug=True)
