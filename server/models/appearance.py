from server.app import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy_serializer import SerializerMixin

class Appearance(db.Model, SerializerMixin):
    __tablename__ = "appearances"

    id = Column(Integer, primary_key= True)
    rating = Column(Integer, nullable=False)

    guest_id = Column(Integer(), ForeignKey("guests.id"))
    episode_id = Column(Integer(), ForeignKey("episodes.id", ondelete="CASCADE"))

    guest = relationship('Guest', back_populates='appearances')
    episode = relationship('Episode', back_populates='appearances')

    @validates('rating')
    def validate_rating(self, key, rating):
        if not (1 <= rating <= 5):
            raise ValueError('Rating must be between 1 and 5.')
        return rating
            