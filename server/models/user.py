from app import db, bcrypt
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique = True)
    password_hash = Column(String)

    def __repr__(self):
        return f'User{self.username}'

    @validates('username')
    def validate_username(self, key, username):
        if not username or len(username) < 4:
            raise ValueError("Username must be at least 4 characters")
        if self.__class__.query.filter_by(username=username).first():
            raise ValueError("Username already exists")
        return username
    
    @property
    def password(self):
        raise AttributeError('password is write-only')
    
    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


    ...