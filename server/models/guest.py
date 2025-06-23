from server.app import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

class Guest(db.Model, SerializerMixin):
    __tablename__ = "guests"

    id = Column(Integer, primary_key= True)
    name = Column(String, nullable= False)
    occupation = Column(String, nullable=False)

    
    appearances = relationship("Appearance", back_populates="guest")
    serialize_rules = ('-appearances.guest',)

    def __repr__(self):
        return f'Guest{self.name}: {self.occupation}'
    ...