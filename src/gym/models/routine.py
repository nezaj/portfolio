from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

from ...data.base import Base
from ...data.mixins import CRUDMixin, FilterMixin

class Routine(Base, CRUDMixin, FilterMixin):
    __tablename__ = "routines"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, unique=True)
