from server.app import db
from sqlalchemy import Column, Integer, Date
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

class Episode(db.Model, SerializerMixin):
    __tablename__ = "episodes"
    
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    number = Column(Integer)

    appearances= relationship('Appearance', back_populates='episode')
    serialize_rules = ('-appearances.episode',)

    def __repr__(self):
        return f'Episode{self.date} {self.number}'
    
