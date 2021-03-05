from db import db

class ShopModel(db.Model):
    __tablename__ = "shop_details"

    shop_name = db.Column(db.String(200),nullable=False)#char(100),
    shop_id =db.Column(db.Integer , primary_key=True)#int PRIMARY KEY,
    shop_address = db.Column(db.String(80),nullable=False)#character,
    pincode =db.Column(db.Integer,nullable=False) #int,
    active = db.Column(db.Boolean,nullable=False)#bool

    @classmethod
    def get_all_shops(cls):
        return cls.query.all()
        
    def save_to_db(self)-> None:
        db.session.add(self)
        db.session.commit()
