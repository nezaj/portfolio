from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

from ...data.base import Base
from ...data.mixins import CRUDMixin, FilterMixin

class Exercise(Base, CRUDMixin, FilterMixin):
    __tablename__ = "exercises"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, unique=True)
