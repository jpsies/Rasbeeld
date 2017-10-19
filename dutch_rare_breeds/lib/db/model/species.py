import uuid
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from .meta import Base, UUID, DBSession


# pylint: disable-msg=too-few-public-methods
class Species(Base):
    __tablename__ = "species"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(String(100))

def get_species(id_):
    return DBSession.query(Species)\
    .filter(Species.id == id_)\
    .first()

def get_species_by_name(name_):
    return DBSession.query(Species)\
    .filter(Species.name == name_)\
    .first()

def get_all_species():
    return DBSession.query(Species)\
    .all()
