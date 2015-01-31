from ..db import db

class FilterMixin(object):
    """Provides convenience functions for filtering models"""

    @classmethod
    def filter_by(cls, **kwargs):
        return db.session.query(cls).filter_by(**kwargs)
