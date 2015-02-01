from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer
from sqlalchemy.orm import relationship

from ...data.base import Base
from ...data.mixins import CRUDMixin, FilterMixin

class Prescription(Base, CRUDMixin, FilterMixin):
    """
    Associates routines with exercises with their perscription info
    """
    __tablename__ = "perscriptions"
    routine_id = Column(Integer, ForeignKey('routines.id'), primary_key=True)
    exercise_id = Column(Integer, ForeignKey('exercises.id'), primary_key=True)
    exercise = relationship("Exercise", foreign_keys=[exercise_id],
                            backref='routine_prescriptions')
    sets = Column('sets', Integer, nullable=False)
    weight = Column('weight', Integer, nullable=False)
    reps = Column('reps', Integer, nullable=False)
    complete_count = Column('complete_count', Integer,
                            nullable=False, default=0)
