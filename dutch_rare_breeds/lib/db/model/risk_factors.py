import uuid
import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from .meta import Base, UUID, DBSession
from .breeds import Breed
from .species import Species

# pylint: disable-msg=too-few-public-methods
class RiskFactor(Base):
    __tablename__ = "risk_factors"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    species = Column(UUID, ForeignKey('species.id'))
    breed = Column(UUID, ForeignKey('breeds.id'))
    name_association = Column(String(100))
    N_breeding_females = Column(Integer)
    N_breeding_males = Column(Integer)
    N_breed_keeping_members = Column(Integer)
    N_active_breeders = Column(Integer)
    continuity_breeding = Column(Integer)
    provinces = Column(String(50))
    breed_present_abroad = Column(Integer)
    abroad_examples = Column(String(200))
    promotion = Column(String(50))
    activities = Column(String(50))
    herdbook = Column(Integer)
    elements_breeding_program = Column(Integer)
    cryobank = Column(Integer)
    breeding_limitations = Column(String(50))
    professional_members = Column(Integer)
    profitable_output = Column(Integer)
    output_examples = Column(String(200))
    specialty_use = Column(Integer)
    specialty_examples = Column(String(200))
    governmental_support = Column(Integer)
    support_examples = Column(String(200))
    timestamp = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    confirmed = Column(Boolean, default=True)

def get_risk_factor(id_):
    return DBSession.query(RiskFactor)\
        .filter(RiskFactor.id == id_)\
        .first()

def get_most_recent_risk_factors_by_breed_id(breed_id, name_association):
    return DBSession.query(RiskFactor)\
        .join(Species)\
        .join(Breed)\
        .filter(Breed.id == breed_id)\
        .filter(RiskFactor.name_association == name_association)\
        .order_by(RiskFactor.timestamp.desc())\
        .first()

def get_breed_by_species_id(species_id):
    return DBSession.query(RiskFactor.breed)\
    .filter(RiskFactor.species == species_id)\
    .all()

def get_association_by_breed_id(breed_id):
    return DBSession.query(RiskFactor.name_association)\
    .filter(RiskFactor.breed == breed_id)\
    .all()
