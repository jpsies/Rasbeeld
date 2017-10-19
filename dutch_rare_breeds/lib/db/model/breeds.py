import uuid
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from .meta import Base, UUID, DBSession


# pylint: disable-msg=too-few-public-methods
class Breed(Base):
    __tablename__ = "breeds"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(String(20))

def get_breed(id_):
    return DBSession.query(Breed)\
    .filter(Breed.id == id_)\
    .first()

def get_breed_by_name(name_):
    return DBSession.query(Breed)\
    .filter(Breed.name == name_)\
    .first()

def get_most_recent_breed():
    return DBSession.query(Breed)\
    .first()
