from sqlalchemy.schema import Column
from sqlalchemy.orm import relation
from sqlalchemy.types import Integer, String

from ...data.base import Base
from ...data.db import db
from ...data.mixins import CRUDMixin, FilterMixin

class Routine(Base, CRUDMixin, FilterMixin):
    __tablename__ = "routines"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, unique=True)
    prescriptions = relation('Prescription', backref='routine')

    def add_prescriptions(self, new_prescriptions):
        """
        Takes a list of prescription objects and appends them
        to routine prescriptions
        """
        self.prescriptions.extend(new_prescriptions)
        db.session.add(self)
        db.session.commit()
