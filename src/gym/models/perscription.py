from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer
from sqlalchemy.orm import relationship

from .exercise import Exercise
from ...data.base import Base
from ...data.mixins import CRUDMixin, FilterMixin

class Perscription(Base, CRUDMixin, FilterMixin):
    __tablename__ = "perscriptions"
    id = Column('id', Integer, primary_key=True)
    exercise_id = Column(Integer, ForeignKey(Exercise.id), nullable=False)
    exercise = relationship("Exercise", foreign_keys=[exercise_id])
    sets = Column('sets', Integer, nullable=False)
    weight = Column('weight', Integer, nullable=False)
    reps = Column('reps', Integer, nullable=False)
    complete_count = Column('complete_count', Integer,
                            nullable=False, default=0)
