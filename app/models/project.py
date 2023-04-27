from sqlalchemy import Column, String, Text

from app.core.db import Base


class Project(Base):
    name = Column(
        String(100),
        nullable=False)
    description = Column(Text)
