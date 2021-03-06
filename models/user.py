from db import db

class UserModel(db.Model):
    __tablename__= "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)

    @classmethod
    def find_by_username(cls,username:str) -> "UserModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls,user_id:int)-> "UserModel":
        return cls.query.filter_by(id=user_id).first()

    def save_to_db(self)-> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self)-> None:
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all_user(cls):
        return cls.query.all()