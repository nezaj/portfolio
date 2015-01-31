from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Date, Integer
from sqlalchemy.orm import relationship

from .exercise import Exercise
from ...data.base import Base
from ...data.mixins import CRUDMixin, FilterMixin

class Entry(Base, CRUDMixin, FilterMixin):
    __tablename__ = "entries"
    id = Column('id', Integer, primary_key=True)
    date = Column('date', Date, nullable=False)
    exercise_id = Column(Integer, ForeignKey(Exercise.id), nullable=False)
    exercise = relationship("Exercise", foreign_keys=[exercise_id])
    sets = Column('sets', Integer, nullable=False)
    weight = Column('weight', Integer, nullable=False)
    reps = Column('reps', Integer, nullable=False)
