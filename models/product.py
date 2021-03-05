from db import db


class ProductModel(db.Model):
    __tablename__="products"
    id = db.Column(db.Integer, primary_key=True)
    product_name =db.Column(db.String(80), nullable=False)
    product_id = db.Column(db.String(80), nullable=False)
    sale_price = db.Column(db.Float, nullable=False)
    mrp= db.Column(db.Float, nullable=False)
    shop_id = db.Column(db.Integer, nullable=False)

    @classmethod
    def get_product_by_id(cls,product_id:str) -> "ProductModel":
        return cls.query.filter_by(product_id=product_id).first()
